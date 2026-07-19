cmake_minimum_required(VERSION 3.20)

project(
	htmlcord
    VERSION 0.1.0
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

add_executable(htmlcord
    src/main.cpp
)

target_include_directories(htmlcord PRIVATE
    src/headers
)

# Put the executable in the project root
set_target_properties(htmlcord PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}"
)
