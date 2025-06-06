# 🛠️ Workshop Parts Locator System
**Find parts instantly with Arduino-powered LED guidance**  
*A Flask web interface to search and light up storage bins by description or image.*


## ✨ Features
- **Web Interface**  
  🔍 Search parts by text description or uploaded image  
  ➕ Add new parts with bin locations  
- **Hardware Integration**  
  💡 Arduino lights up LEDs to pinpoint the correct bin  
  🖨️ 3D-printable mounts for clean LED installation  
- **Database**  
  📦 SQLite storage for part details and locations  

## 🚀 Quick Start
### Hardware Setup
1. Upload `arduino/led_control.ino` to your Arduino
2. Wire LEDs to pins D2-D5 (or customize in code)

### Software Setup
```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run the Flask server
python backend/app.py
