# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files

# Collect Plotly data files including validators
plotly_datas = collect_data_files('plotly')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=plotly_datas,
    hiddenimports=[
        'ttkbootstrap',
        'pandas',
        'scipy',
        'plotly',
        'plotly.validators',
        'plotly.graph_objects',
        'plotly.express',
        'pydub',
        'numpy',
        'gui',
        'config',
        'bpm_analysis',
        'heartbeat_labeler',
        'PIL',
        'PIL._tkinter_finder'
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
    a.binaries,
    a.datas,
    [],
    name='BPM_Analyzer',
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
) 