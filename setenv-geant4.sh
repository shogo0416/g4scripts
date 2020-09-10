#===============================================================================
#
# Geant4 setup script
# Author: Shogo OKADA (KEK-CRC, shogo.okada@kek.jp), 2020-09
#
#===============================================================================
# set Geant4 install directory
G4DIR_PREFIX=/opt/geant4
#===============================================================================
# Never touch below!!!
G4VERSION="$1"

if [ "$G4VERSION" = "" ] || [ "$G4VERSION" = "help" ]; then
  echo "
  [Usage]
    - Sequentian mode
      $ source setenv-geant4.sh <version>

    - Multi-thread mode
      $ source setenv-geant4.sh <version> MT

    - Print G4 versions installed
      $ source setenv-geant4.sh list

    - Print this information
      $ source setenv-geant4.sh help
  "
  return
elif [ "$G4VERSION" = "list" ]; then
  ls --ignore={build,data,src} $G4DIR_PREFIX
  return
fi

MULTITHREAD="$2"

if [ "$MULTITHREAD" = "MT" ]; then
  G4DIR=$G4DIR_PREFIX/$G4VERSION-mt
elif [ "$MULTITHREAD" = "" ]; then
  G4DIR=$G4DIR_PREFIX/$G4VERSION
fi

# check install directory
if [ ! -e $G4DIR ]; then
  echo "[ERROR] Not found: $G4DIR"
  return
fi

# set path to Geant4
if [ "$MULTITHREAD" = "MT" ]; then
  echo "
  Set environment for Geant4 $G4VERSION multi-threading mode
  "
elif [ "$MULTITHREAD" = "" ]; then
  echo "
  Set environment for Geant4 $G4VERSION sequential mode
  "
fi

source $G4DIR/bin/geant4.sh
env | grep G4
