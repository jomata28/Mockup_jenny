# Supreme AI Council - Deployment Guide

**Version**: 1.0
**Last Updated**: 2026-01-19
**Purpose**: Deploy your agent council to run 24/7 on cloud infrastructure

---

## Deployment Overview

This guide walks you through deploying the Supreme AI Council to a cloud server that runs continuously, accessible via Telegram from anywhere.

**Architecture**:
```
┌──────────────┐
│     YOU      │ ← Telegram app on phone/desktop
└──────┬───────┘
       │ HTTPS
       ▼
┌──────────────────────┐
│  Telegram Bot API    │
└──────────┬───────────┘
           │ Webhook
           ▼
┌───────────────────────────────┐
│   CLOUD SERVER (24/7)         │
│                               │
│  ┌─────────────────────────┐ │
│  │  Nginx (Reverse Proxy)  │ │
│  └────────┬────────────────┘ │
│           │
│  │  ┌─────▼──────────────┐  │
│  │  │ Telegram Webhook   │  │
│  │  │  Handler (Python)  │  │
│  │  └──────┬─────────────┘  │
│  │         │                 │
│  │  ┌──────▼──────────────┐ │
│  │  │   JENI (Primary)    │ │
│  │  │   Agent Process     │ │
│  │  └──────┬──────────────┘ │
│  │         │  Delegates      │
│  │    ┌────┴────┬────┬────┬─┴─┐
│  │    ▼         ▼    ▼    ▼   ▼
│  │  [Aristóteles][Asklepai][Airquimides]
│  │  [Seshait][Vulkain]    │ │
│  │    │         │    │    │   │
│  │    └─────────┴────┴────┴───┘
│  │              │               │
│  │         ┌────▼──────┐        │
│  │         │ MCP Layer │        │
│  │         └────┬──────┘        │
│  │              │               │
│  └──────────────┼───────────────┘
                  │ API calls
                  ▼
       ┌──────────────────┐
       │  Notion API      │
       │  (Your Databases)│
       └──────────────────┘
```

---

## Prerequisites

### 1. Cloud Server Requirements

**Minimum Specs**:
- **CPU**: 2 vCPU cores
- **RAM**: 4 GB
- **Storage**: 20 GB SSD
- **OS**: Ubuntu 22.04 LTS or later
- **Network**: Static IP address

**Recommended Providers**:
- **DigitalOcean**: Droplet ($24/month for 2GB, $48/month for 4GB)
- **AWS**: EC2 t3.medium ($30-40/month)
- **Linode**: Shared CPU 4GB ($24/month)
- **Vultr**: Cloud Compute 4GB ($24/month)

**Cost Estimate**: $25-50/month for reliable 24/7 operation

### 2. Domain Name (Optional but Recommended)

For HTTPS webhook:
- Purchase domain: Namecheap, Google Domains, etc. (~$12/year)
- Point A record to your server IP
- Example: `council.yourdomain.com`

### 3. Accounts & API Keys

- [ ] Telegram Bot Token (from @BotFather)
- [ ] Notion API Key (from notion.so/my-integrations)
- [ ] Cloud provider account
- [ ] GitHub account (for code deployment)

---

## Step-by-Step Deployment

### Step 1: Provision Cloud Server

**DigitalOcean Example**:
1. Create account at digitalocean.com
2. Create new Droplet
3. Choose: Ubuntu 22.04 LTS
4. Plan: Basic, 4GB RAM / 2 vCPU ($24/month)
5. Datacenter: Choose closest to you
6. Authentication: SSH Key (generate if needed)
7. Create Droplet
8. Note the IP address

**SSH into server**:
```bash
ssh root@YOUR_SERVER_IP
```

### Step 2: Initial Server Setup

**Update system**:
```bash
apt update && apt upgrade -y
```

**Install dependencies**:
```bash
# Python 3.11+
apt install -y python3.11 python3.11-venv python3-pip

# Node.js (for MCP servers)
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# Git
apt install -y git

# Nginx (reverse proxy)
apt install -y nginx

# Certbot (for HTTPS)
apt install -y certbot python3-certbot-nginx

# Docker (optional, for containerized deployment)
apt install -y docker.io docker-compose
systemctl enable docker
systemctl start docker
```

**Create non-root user** (security best practice):
```bash
adduser council
usermod -aG sudo council
usermod -aG docker council

# Switch to new user
su - council
```

### Step 3: Clone Repository

```bash
cd /home/council
git clone https://github.com/yourusername/Mockup_jenny.git
cd Mockup_jenny/Supreme_Council
```

### Step 4: Environment Configuration

**Create .env file**:
```bash
nano .env
```

**Add secrets** (replace with your actual values):
```bash
# Telegram
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather

# Authentication
SUPREME_COUNCIL_PIN_HASH=your_pin_hash_from_setup

# Notion
NOTION_API_KEY=secret_your_notion_api_key

# MCP Configuration
MCP_CONFIG_PATH=/home/council/Mockup_jenny/Supreme_Council/.mcp/config.json

# Logging
LOG_LEVEL=INFO
LOG_FILE=/var/log/supreme_council/council.log

# Server
WEBHOOK_URL=https://council.yourdomain.com/webhook
PORT=8443
```

**Secure the .env file**:
```bash
chmod 600 .env
```

### Step 5: Install Python Dependencies

**Create virtual environment**:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

**Create requirements.txt**:
```bash
cat > requirements.txt <<EOF
python-telegram-bot==20.7
python-dotenv==1.0.0
requests==2.31.0
anthropic==0.18.1
pydantic==2.5.3
aiohttp==3.9.1
EOF
```

**Install**:
```bash
pip install -r requirements.txt
```

### Step 6: Setup MCP Servers

**Create MCP config**:
```bash
mkdir -p .mcp
nano .mcp/config.json
```

**Add MCP configuration**:
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/council/Documents"
      ]
    }
  }
}
```

**Install MCP servers globally**:
```bash
sudo npm install -g @notionhq/notion-mcp-server
sudo npm install -g @modelcontextprotocol/server-filesystem
```

**Test MCP**:
```bash
npx @notionhq/notion-mcp-server
# Should connect without errors
# Ctrl+C to stop
```

### Step 7: Setup Nginx Reverse Proxy

**Create Nginx config**:
```bash
sudo nano /etc/nginx/sites-available/supreme-council
```

**Add configuration**:
```nginx
server {
    listen 80;
    server_name council.yourdomain.com;

    location /webhook {
        proxy_pass http://localhost:8443;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location / {
        return 404;
    }
}
```

**Enable site**:
```bash
sudo ln -s /etc/nginx/sites-available/supreme-council /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl reload nginx
```

**Setup HTTPS with Let's Encrypt**:
```bash
sudo certbot --nginx -d council.yourdomain.com
```

Follow prompts. Certbot will automatically configure HTTPS.

### Step 8: Configure Systemd Service

**Create service file**:
```bash
sudo nano /etc/systemd/system/supreme-council.service
```

**Add configuration**:
```ini
[Unit]
Description=Supreme AI Council - Agent System
After=network.target

[Service]
Type=simple
User=council
Group=council
WorkingDirectory=/home/council/Mockup_jenny/Supreme_Council
Environment="PATH=/home/council/Mockup_jenny/Supreme_Council/venv/bin:/usr/local/bin:/usr/bin:/bin"
EnvironmentFile=/home/council/Mockup_jenny/Supreme_Council/.env
ExecStart=/home/council/Mockup_jenny/Supreme_Council/venv/bin/python3 main.py
Restart=always
RestartSec=10
StandardOutput=append:/var/log/supreme_council/council.log
StandardError=append:/var/log/supreme_council/error.log

[Install]
WantedBy=multi-user.target
```

**Create log directory**:
```bash
sudo mkdir -p /var/log/supreme_council
sudo chown council:council /var/log/supreme_council
```

**Enable and start service**:
```bash
sudo systemctl daemon-reload
sudo systemctl enable supreme-council
sudo systemctl start supreme-council
```

**Check status**:
```bash
sudo systemctl status supreme-council
```

**View logs**:
```bash
sudo journalctl -u supreme-council -f
# Or
tail -f /var/log/supreme_council/council.log
```

### Step 9: Setup Telegram Webhook

**Set webhook** (one-time):
```bash
curl -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setWebhook" \
  -d "url=https://council.yourdomain.com/webhook" \
  -d "allowed_updates=[\"message\",\"callback_query\"]"
```

**Verify webhook**:
```bash
curl "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getWebhookInfo"
```

Should show your webhook URL and `pending_update_count: 0`.

### Step 10: Test End-to-End

**Send message to your bot**:
1. Open Telegram
2. Search for your bot (@yourbotname)
3. Send: "Hello"
4. Bot should respond: "Please enter your 4-digit PIN to continue."
5. Enter your PIN
6. Bot should respond: "✅ Authenticated. How can I assist you?"

**Check logs for any errors**:
```bash
tail -f /var/log/supreme_council/council.log
```

---

## Alternative: Docker Deployment

For easier deployment and isolation:

**Create Dockerfile**:
```dockerfile
FROM python:3.11-slim

# Install Node.js for MCP servers
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install MCP servers
RUN npm install -g @notionhq/notion-mcp-server \
    @modelcontextprotocol/server-filesystem

# Copy application code
COPY . .

# Expose port
EXPOSE 8443

# Run application
CMD ["python", "main.py"]
```

**Create docker-compose.yml**:
```yaml
version: '3.8'

services:
  supreme-council:
    build: .
    container_name: supreme-council
    restart: always
    ports:
      - "8443:8443"
    env_file:
      - .env
    volumes:
      - ./logs:/var/log/supreme_council
      - ./data:/app/data
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

**Deploy**:
```bash
docker-compose up -d
```

**View logs**:
```bash
docker-compose logs -f
```

---

## Monitoring & Maintenance

### Health Checks

**Create health check script**:
```bash
#!/bin/bash
# health_check.sh

# Check if service is running
if ! systemctl is-active --quiet supreme-council; then
    echo "❌ Supreme Council service is down"
    systemctl restart supreme-council
    # Send alert via Telegram or email
    exit 1
fi

# Check if webhook is responsive
if ! curl -sf https://council.yourdomain.com/health > /dev/null; then
    echo "❌ Webhook not responding"
    exit 1
fi

echo "✅ System healthy"
exit 0
```

**Schedule with cron** (every 5 minutes):
```bash
crontab -e

# Add:
*/5 * * * * /home/council/health_check.sh >> /var/log/supreme_council/health.log 2>&1
```

### Log Rotation

**Create logrotate config**:
```bash
sudo nano /etc/logrotate.d/supreme-council
```

**Add**:
```
/var/log/supreme_council/*.log {
    daily
    rotate 30
    compress
    delaycompress
    notifempty
    create 0640 council council
    sharedscripts
    postrotate
        systemctl reload supreme-council > /dev/null 2>&1 || true
    endscript
}
```

### Automatic Updates

**Create update script**:
```bash
#!/bin/bash
# update.sh

cd /home/council/Mockup_jenny
git pull origin main

cd Supreme_Council
source venv/bin/activate
pip install -r requirements.txt --upgrade

sudo systemctl restart supreme-council

echo "✅ Update complete"
```

**Schedule weekly updates** (Sundays at 3 AM):
```bash
crontab -e

# Add:
0 3 * * 0 /home/council/update.sh >> /var/log/supreme_council/updates.log 2>&1
```

### Backup Strategy

**Daily Notion backup** (handled by agents)
**Weekly server snapshot** (cloud provider feature)
**Monthly off-site backup**:

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR=/home/council/backups
DATE=$(date +%Y%m%d)

mkdir -p $BACKUP_DIR

# Backup configuration
tar -czf $BACKUP_DIR/config-$DATE.tar.gz \
    /home/council/Mockup_jenny/Supreme_Council/.env \
    /home/council/Mockup_jenny/Supreme_Council/.mcp/ \
    /home/council/Mockup_jenny/Supreme_Council/auth/

# Backup logs
tar -czf $BACKUP_DIR/logs-$DATE.tar.gz \
    /var/log/supreme_council/

# Upload to cloud storage (S3, Dropbox, etc.)
# aws s3 cp $BACKUP_DIR s3://your-backup-bucket/ --recursive

# Clean old backups (keep 30 days)
find $BACKUP_DIR -type f -mtime +30 -delete

echo "✅ Backup complete: $DATE"
```

---

## Security Hardening

### 1. Firewall Configuration

```bash
# Install UFW
sudo apt install -y ufw

# Allow SSH
sudo ufw allow 22/tcp

# Allow HTTP/HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable firewall
sudo ufw enable
```

### 2. Fail2Ban (Prevent Brute Force)

```bash
sudo apt install -y fail2ban

sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

### 3. Automatic Security Updates

```bash
sudo apt install -y unattended-upgrades

sudo dpkg-reconfigure --priority=low unattended-upgrades
```

### 4. SSH Key-Only Authentication

```bash
sudo nano /etc/ssh/sshd_config

# Set:
PasswordAuthentication no
PermitRootLogin no

sudo systemctl restart sshd
```

### 5. API Key Rotation

**Quarterly**:
- Rotate Notion API key
- Regenerate Telegram bot token
- Update PIN hash

---

## Troubleshooting

### Issue: Agents not responding

**Check service status**:
```bash
sudo systemctl status supreme-council
```

**Check logs**:
```bash
sudo journalctl -u supreme-council -n 100 --no-pager
```

**Common causes**:
- Invalid environment variables
- MCP server not running
- Notion API rate limiting
- Webhook not set correctly

### Issue: Webhook failing

**Verify webhook**:
```bash
curl https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getWebhookInfo
```

**Check Nginx**:
```bash
sudo nginx -t
sudo systemctl status nginx
```

**Check SSL certificate**:
```bash
sudo certbot certificates
```

### Issue: High memory usage

**Check resource usage**:
```bash
htop  # or top
```

**Restart service**:
```bash
sudo systemctl restart supreme-council
```

**Consider upgrading server** if consistently >80% memory.

---

## Cost Optimization

**Reduce costs**:
1. **Right-size server**: Start with 2GB RAM, upgrade if needed
2. **Reserved instances**: Pre-pay for 1 year (20-30% discount)
3. **Shutdown during dev**: Stop server when not using (dev only)
4. **API call optimization**: Cache data, reduce Notion queries
5. **Log management**: Limit log retention to 30 days

**Monthly cost breakdown**:
- Server: $24-48/month
- Domain: $1/month (paid annually)
- Backup storage: $2-5/month
- **Total**: ~$30-55/month

---

## Production Checklist

Before going live:

- [ ] Server provisioned and secured
- [ ] SSH key-only authentication configured
- [ ] Firewall rules set
- [ ] Nginx installed and configured with HTTPS
- [ ] All environment variables set correctly
- [ ] MCP servers tested and working
- [ ] Telegram webhook set and verified
- [ ] All agents can access Notion databases
- [ ] PIN authentication working
- [ ] Systemd service enabled and running
- [ ] Health checks configured
- [ ] Log rotation configured
- [ ] Backup strategy implemented
- [ ] Monitoring alerts set up
- [ ] Documentation updated with your specific details

---

## Support Resources

- **Telegram Bot API**: https://core.telegram.org/bots/api
- **Notion API**: https://developers.notion.com
- **MCP Docs**: https://github.com/modelcontextprotocol
- **Ubuntu Server Guide**: https://ubuntu.com/server/docs
- **Nginx Docs**: https://nginx.org/en/docs
- **Let's Encrypt**: https://letsencrypt.org/docs

---

*Your Supreme AI Council is now running 24/7. Access it anytime via Telegram.*
