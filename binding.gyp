{
  "targets": [{
    "target_name": "node-libuiohook",
    "include_dirs" : [
      "source",
      "<!(node -e \"require('nan')\")"
    ],
    "sources": [
      "source/hook.cpp",
      "source/module.cpp",
    ],
    "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS", "UNICODE"],
    "cflags!": [
        "-fno-exceptions"
    ],
    "cflags_cc!": [
        "-fno-exceptions"
    ],
    "conditions": [
      [
        "OS=='win'", {
          "defines": [
              "_UNICODE",
              "_WIN32_WINNT=0x0601"
            ],
          "configurations": {
            "Release": {
              "msvs_settings": {
                "VCCLCompilerTool" : {
                  "ExceptionHandling": 1,
                }
              }
            },
            "Debug": {
              "msvs_settings": {
                "VCCLCompilerTool" : {
                  "ExceptionHandling": 1,
                }
              }
            }
          }
        }
      ]
    ]
  }]
}