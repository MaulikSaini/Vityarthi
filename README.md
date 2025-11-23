# 📚 Vityarthi - School Timetable Notification System

**Vityarthi** (विद्यार्थी - meaning "Student" in Hindi) is an automated desktop notification system that helps students stay on track with their class schedule. Never miss a class again with timely reminders sent directly to your desktop!



## 📋 Description

Vityarthi is a Python-based notification system that automatically tracks your school timetable and sends desktop notifications before each class period. The system monitors the current day and time, then displays reminders showing the subject name and class timing, helping students maintain punctuality and stay organized throughout the school day.

## ✨ Features

- 🔔 **Automated Notifications** - Desktop alerts for each class period
- 📅 **Weekly Schedule Support** - Different timetables for each day of the week
- ⏰ **Time-Based Triggers** - Notifications at 8:00 AM, 9:30 AM, and 11:00 AM
- 🌐 **Cross-Platform** - Works on Windows, macOS, and Linux
- 📊 **Multi-Subject Tracking** - Supports multiple subjects across different days
- 🎯 **Sunday Detection** - Special handling for non-school days
- 💻 **Lightweight** - Minimal system resource usage

## 🎯 Current Timetable

### Weekday Schedule

| Time | Period | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|------|--------|--------|---------|-----------|----------|--------|----------|
| 8:00-9:00 | Period 1 | Hindi | Science | Maths | Hindi | Science | Maths |
| 9:30-10:30 | Period 2 | English | SST | Science | English | SST | Science |
| 11:00-12:00 | Period 3 | Maths | IT | English | Maths | IT | English |

**Sunday**: No classes - System will notify and stop

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the repository:**
```bash
git clone <repository-url>
cd vityarthi
```

2. **Install required dependencies:**
```bash
pip install plyer
```

3. **Run the application:**
```bash
python vityarthi.py
```

### Quick Install (One-liner)
```bash
pip install plyer && python vityarthi.py
```

## 💡 How It Works

1. **Day Detection**: The system automatically detects the current day of the week
2. **Time Monitoring**: Continuously monitors system time for period start times
3. **Schedule Loading**: Loads the appropriate timetable based on the current day
4. **Notification Delivery**: Sends desktop notifications with subject name and timing
5. **Auto-Sleep**: Waits 40 minutes between checks to conserve resources
6. **Loop Continuation**: Repeats for all three periods, then exits

### Notification Example

```
Title: Hindi
Message: Time:- 8:00 - 9:00
Duration: 60 seconds
```

## 📁 Project Structure

```
vityarthi/
│
├── vityarthi.py          # Main application file
├── README.md             # This file
└── requirements.txt      # Python dependencies (optional)
```

## 🔧 Technical Details

### Dependencies

| Package | Purpose | Installation |
|---------|---------|--------------|
| `datetime` | Date and time handling | Built-in |
| `time` | Sleep functionality | Built-in |
| `plyer` | Desktop notifications | `pip install plyer` |

### Code Architecture

**Key Components:**
- **Timetable Lists**: Six separate lists for Monday through Saturday schedules
- **Period Timer**: Tracks which period is currently active (0, 1, or 2)
- **Day Function**: Converts datetime object to readable day names
- **Main Loop**: Continuous monitoring and notification system

**Time Triggers:**
```python
8:00 AM  → Period 1 notification
9:30 AM  → Period 2 notification
11:00 AM → Period 3 notification
```

## ⚙️ Configuration

### Customizing Your Timetable

To modify the schedule, edit the following lists in `vityarthi.py`:

```python
# Example: Modify Monday schedule
mon = ["Hindi", "English", "Maths"]

# Example: Change period timings
periods_time = [
    "Time:- 8:00 - 9:00",
    "Time:- 9:30 - 10:30",
    "Time:- 11:00 - 12:00"
]
```

### Adding More Periods

To add additional periods, extend the time checking logic:

```python
if t.hour == 13 and t.minute == 0:  # 1:00 PM
    i = 3
    timer = periods_time[3]
```

## 🐛 Known Issues

1. **Hard-coded Schedule**: Timetable must be manually edited in code
2. **Fixed Sleep Duration**: Uses 40-minute sleep intervals
3. **No Pause Feature**: Cannot temporarily disable notifications
4. **No Holiday Support**: Runs on all weekdays regardless of holidays
5. **Single Schedule**: Only supports one timetable at a time

## 🔮 Future Enhancements

### Planned Features
- [ ] JSON/YAML configuration file for easy schedule editing
- [ ] GUI interface for timetable management
- [ ] Holiday calendar integration
- [ ] Multiple schedule profiles (exam schedule, regular schedule, etc.)
- [ ] Sound notifications in addition to desktop alerts
- [ ] 5-minute advance warning notifications
- [ ] Break time reminders
- [ ] Homework and assignment tracking
- [ ] Web-based dashboard for remote schedule updates
- [ ] Mobile app companion

### Technical Improvements
- [ ] Event-driven architecture (eliminate sleep-based checking)
- [ ] Database integration for schedule storage
- [ ] Logging system for notification history
- [ ] Error handling and graceful failure management
- [ ] Background service/daemon mode
- [ ] Multi-language support
- [ ] Cloud synchronization across devices

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Contribution Ideas
- Add configuration file support
- Create a GUI interface
- Improve notification system
- Add unit tests
- Write documentation
- Report bugs

## 📝 Usage Tips

### Running on Startup (Auto-start)

**Windows:**
1. Create a shortcut to `vityarthi.py`
2. Press `Win + R`, type `shell:startup`, press Enter
3. Place the shortcut in the Startup folder

**macOS:**
1. Open System Preferences → Users & Groups
2. Click your username → Login Items
3. Click '+' and add `vityarthi.py`

**Linux (Ubuntu):**
1. Open Startup Applications
2. Add command: `python3 /path/to/vityarthi.py`

### Running in Background

**Using nohup (Linux/macOS):**
```bash
nohup python3 vityarthi.py &
```

**Using screen:**
```bash
screen -S vityarthi
python3 vityarthi.py
# Press Ctrl+A, then D to detach
```

## 🔒 Privacy & Security

- ✅ All data stored locally on your machine
- ✅ No internet connection required
- ✅ No data collection or transmission
- ✅ No administrative privileges needed
- ✅ Open source and transparent code

## 🧪 Testing

### Manual Testing Checklist
- [ ] Verify notifications appear at correct times
- [ ] Check correct schedule loads for each day
- [ ] Test Sunday special notification
- [ ] Confirm notification timeout works
- [ ] Validate all period transitions
- [ ] Test schedule accuracy for all subjects

### Time-Based Testing
To test without waiting for actual class times, temporarily modify:
```python
if t.hour == 8:  # Change to current hour for testing
```

## 📖 Requirements File

Create a `requirements.txt` file:
```
plyer==2.1.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## ❓ FAQ

**Q: Can I change the notification duration?**  
A: Yes, modify the `timeout` parameter in the `notification.notify()` call.

**Q: Will this work on my operating system?**  
A: Yes! Plyer supports Windows, macOS, and Linux desktop notifications.

**Q: How do I stop the program?**  
A: Press `Ctrl + C` in the terminal, or close the terminal window.

**Q: Can I add more than 3 periods?**  
A: Yes, extend the `periods_time` list and add corresponding time checks.

**Q: Does this affect system performance?**  
A: No, the program is lightweight and sleeps between checks.

## 🙏 Acknowledgments

- **Plyer** - Cross-platform Python library for desktop notifications
- **Python Community** - For excellent documentation and support
- Inspired by the need for better time management in education



## 👤 Author

Maulik Saini
- GitHub: [@MaulikSaini](https://github.com/MaulikSaini)

---

**Made with ❤️ for students, by students**

*Vityarthi - Because every class counts!* 📚⏰✨
