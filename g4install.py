#!/bin/env python3

#===============================================================================
#
# Geant4 Install Script
#
# Author: Shogo OKADA (KEK-CRC, shogo.okada@kek.jp), 2020-09
#
#===============================================================================

import os
import os.path

WITH_QT = True
INSTALL_DATA = True
G4VER = ["10.05.p01", "10.06.ref-08"]
G4DIR = ["10.5.1", "10.6.ref8"]

#-------------------------------------------------------------------------------
def install(install_dir, version, install_data, multi_thread):

  qt_install_path   = '/usr'
  data_install_path = '/opt/geant4/data'
  g4_install_path   = '/opt/geant4/' + install_dir
  g4_source_path    = '../../src/geant4.' + version

  cmd = 'cmake3 -Wno-dev -Wunused-result '

  # X11
  cmd += '-DGEANT4_USE_OPENGL_X11=ON '

  # multi-threading mode
  if not multi_thread:
    cmd += '-DGEANT4_BUILD_MULTITHREADED=OFF '
  else:
    cmd += '-DGEANT4_BUILD_MULTITHREADED=ON '

  # install data
  if not install_data:
    cmd += '-DGEANT4_INSTALL_DATA=OFF '
  else:
    cmd += '-DGEANT4_INSTALL_DATA=ON '

  # set up data directory
  cmd += '-DGEANT4_INSTALL_DATADIR=' + data_install_path + ' '

  # set up QT
  if WITH_QT:
    cmd += '-DGEANT4_USE_QT=ON '
    cmd += '-DCMAKE_PREFIX_PATH=' + qt_install_path + ' '

  # set up Geant4 install directory
  cmd += '-DCMAKE_INSTALL_PREFIX=' + g4_install_path + ' '
  cmd += g4_source_path + ' '

  # log
  cmd += '2>&1 | tee cmake.log'

  # cmake
  print(cmd)
  os.system(cmd)

  # make
  cmd = 'make -j10 2>&1 | tee make.log'
  print(cmd)
  os.system(cmd)

  # make install
  cmd = 'make install 2>&1 | tee install.log'
  print(cmd)
  os.system(cmd)

#-------------------------------------------------------------------------------
def main():

  for install_dir, version in zip(G4DIR, G4VER):

    for multi_thread in [False, True]:

      if multi_thread:
        install_dir += "-mt"

      if not os.path.isdir(install_dir):
        os.mkdir(install_dir)

      os.chdir(install_dir)

      install(install_dir, version, INSTALL_DATA, multi_thread)

      os.chdir("../")

#===============================================================================
if __name__ == "__main__":
  main()
