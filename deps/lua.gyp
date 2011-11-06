{
  'target_defaults': {
    'conditions': [
      ['OS != "win"', {
        'defines': [
          'LUA_USE_POPEN',
        ],
      },
      ],
    ],
  },

  'targets': [
    {
      'target_name': 'lua',
      'type': 'static_library',
      'sources': [
        'lua/src/lapi.c',
        'lua/src/lauxlib.c',
        'lua/src/lbaselib.c',
        'lua/src/lcode.c',
        'lua/src/ldblib.c',
        'lua/src/ldebug.c',
        'lua/src/ldo.c',
        'lua/src/ldump.c',
        'lua/src/lfunc.c',
        'lua/src/lgc.c',
        'lua/src/linit.c',
        'lua/src/liolib.c',
        'lua/src/llex.c',
        'lua/src/lmathlib.c',
        'lua/src/lmem.c',
        'lua/src/lobject.c',
        'lua/src/lopcodes.c',
        'lua/src/loslib.c',
        'lua/src/lparser.c',
        'lua/src/lstate.c',
        'lua/src/lstring.c',
        'lua/src/lstrlib.c',
        'lua/src/ltable.c',
        'lua/src/ltablib.c',
        'lua/src/ltm.c',
        'lua/src/lundump.c',
        'lua/src/lvm.c',
        'lua/src/lzio.c',
      ],

      'sources__52': [
        'lua/src/lapi.c',
        'lua/src/lauxlib.c',
        'lua/src/lbaselib.c',
        'lua/src/lbitlib.c',
        'lua/src/lcode.c',
        'lua/src/lcorolib.c',
        'lua/src/lctype.c',
        'lua/src/ldblib.c',
        'lua/src/ldebug.c',
        'lua/src/ldo.c',
        'lua/src/ldump.c',
        'lua/src/lfunc.c',
        'lua/src/lgc.c',
        'lua/src/linit.c',
        'lua/src/liolib.c',
        'lua/src/llex.c',
        'lua/src/lmathlib.c',
        'lua/src/lmem.c',
        'lua/src/loadlib.c',
        'lua/src/lobject.c',
        'lua/src/lopcodes.c',
        'lua/src/loslib.c',
        'lua/src/lparser.c',
        'lua/src/lstate.c',
        'lua/src/lstring.c',
        'lua/src/lstrlib.c',
        'lua/src/ltable.c',
        'lua/src/ltablib.c',
        'lua/src/ltm.c',
        'lua/src/lundump.c',
        'lua/src/lvm.c',
        'lua/src/lzio.c',
        ],
      'include_dirs': [
          'lua/src',
        ],
      'direct_dependent_settings': {
          'include_dirs': [
            'lua/src',
          ],
        },
    },
  ],
}

