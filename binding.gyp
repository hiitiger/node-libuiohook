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
    ]
  }]
}