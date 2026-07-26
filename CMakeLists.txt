cmake_minimum_required(VERSION 3.10)
project(rb-filterdiff NONE)          # NONE: all scripts, no compiler needed

include(GNUInstallDirs)

# Directory the named filter helpers get installed into. Baked into the
# rb-filterdiff wrapper so it can find them at runtime (they are not on PATH).
set(FILTERDIR "${CMAKE_INSTALL_FULL_LIBEXECDIR}/rb-filterdiff")
configure_file(rb-filterdiff.in rb-filterdiff @ONLY)

install(PROGRAMS "${CMAKE_CURRENT_BINARY_DIR}/rb-filterdiff"
        DESTINATION "${CMAKE_INSTALL_BINDIR}")

file(GLOB filters "${CMAKE_CURRENT_SOURCE_DIR}/filter/*")
install(PROGRAMS ${filters}
        DESTINATION "${CMAKE_INSTALL_LIBEXECDIR}/rb-filterdiff")
