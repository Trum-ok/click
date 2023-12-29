# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('MaterialDark.qss', '.'), ('guardian.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GClick',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['guardian.png'],
)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='click')
app = BUNDLE(coll,
             name='click.app',
             icon='guardian.png',
             bundle_identifier=None,
             info_plist={
                'CFBundleDisplayName': 'click',
                'CFBundleExecutable': 'GClick',
                'CFBundleName': 'click',
                'CFBundleTypeIconFile': 'guardian.png',
                'CFBundlePackageType': 'APPL',
                'CFBundleVersionString': '1.1.0',
                'CFBundleShortVersionString': '1.1.0',
                'NSPrincipalClass': 'NSApplication',
                'NSAppleScriptEnabled': False,
                'NSHighResolutionCapable': True,
            },)
