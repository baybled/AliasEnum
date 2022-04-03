# AliasEnum
Simple python enumerator for online asliases with 2 word split

# Installation

git clone https://github.com/baybled/AliasEnum.git

cd AliasEnum

chmod +x ./aliasEnum.py

./aliasEnum.py $alias1 $alias2 $alias3

# Usage Example 

![alt text](https://raw.githubusercontent.com/baybled/AliasEnum/main/example%20picture.png'?raw=true)

./aliasEnum.py nCux Track2 2Pac

_output_

- nCux
- nTrack
- n2
- nPac
- Cuxn
- CuxTrack
- Cux2
- CuxPac
- Trackn
- TrackCux
- Track2
- TrackPac
- 2n
- 2Cux
- 2Track
- 2Pac
- PacCux
- PacTrack
- Pac2

# Future

- split aliases of 2+ words, output shows 2+ word combos
- combos observe word symmetry (e.g. xx_little_lover_xx preserves xx at the start and end for new combos)

# Troubleshooting

python3 must be located in /usr/bin/python3
