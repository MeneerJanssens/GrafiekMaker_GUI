# Building Executable Guide

## Quick Start
Your executable is ready! Located at:
```
dist\GrafiekMaker.exe
```

## How to Use
1. Navigate to the `dist` folder
2. Double-click `GrafiekMaker.exe` to run
3. The application will start without needing Python installed

## Distribution
You can share `GrafiekMaker.exe` with anyone - they don't need Python or any dependencies installed!

## Rebuilding the Executable

If you make changes to the code, rebuild with:
```bash
.venv\Scripts\python.exe -m PyInstaller --onefile --windowed --clean --name "GrafiekMaker" GrafiekMakerGUI.py
```

### Build Options Explained
- `--onefile`: Creates a single executable file (easier to distribute)
- `--windowed`: No console window appears (GUI-only mode)
- `--name "GrafiekMaker"`: Names the executable "GrafiekMaker.exe"

## File Structure After Build
```
GrafiekMaker_GUI/
├── dist/
│   └── GrafiekMaker.exe          ← Your executable (distribute this!)
├── build/                         ← Temporary build files (can delete)
├── GrafiekMaker.spec             ← PyInstaller configuration
├── GrafiekMakerGUI.py            ← Source code
└── requirements.txt              ← Python dependencies
```

## Tips
- The `.exe` file is ~20-30 MB (includes Python and all libraries)
- First launch may be slower (Windows security scan)
- You can delete the `build` folder to save space
- Keep the `.spec` file if you want to customize the build

## Troubleshooting
If the executable doesn't work:
1. Check Windows Defender didn't block it
2. Try running as administrator
3. Rebuild with: `pyinstaller GrafiekMaker.spec`
