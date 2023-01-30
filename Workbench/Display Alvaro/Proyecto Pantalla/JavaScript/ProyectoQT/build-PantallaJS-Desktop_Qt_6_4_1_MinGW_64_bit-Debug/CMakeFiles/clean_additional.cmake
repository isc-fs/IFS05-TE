# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\PantallaJS_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\PantallaJS_autogen.dir\\ParseCache.txt"
  "PantallaJS_autogen"
  )
endif()
