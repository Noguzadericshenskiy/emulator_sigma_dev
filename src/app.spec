# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('root_window.py', '.'),
        ('icons', 'icons'),
        ('ui', 'ui'),
        ('devices', 'devices'),
        ('utilites', 'utilites'),
    ],
    hiddenimports=[
        'root_window.py',
        'loguru',
        'sqlalchemy',
        'serial',
        'pymodbus',
        'pymodbus.datastore',
        'pymodbus.server',
        'serial.tools.list_ports_windows',
        'devices',
        'devices.registers_devises',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Emulator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,

)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Emulator',
)
