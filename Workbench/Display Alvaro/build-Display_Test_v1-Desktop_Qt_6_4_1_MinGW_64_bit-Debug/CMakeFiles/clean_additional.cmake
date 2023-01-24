# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\Display_Test_v1_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Display_Test_v1_autogen.dir\\ParseCache.txt"
  "Display_Test_v1_autogen"
  )
endif()
