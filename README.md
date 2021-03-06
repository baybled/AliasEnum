# AliasEnum
Simple python enumerator for online asliases with 2 word split

# Installation

git clone https://github.com/baybled/AliasEnum.git

cd AliasEnum

chmod +x ./aliasEnum.py

./aliasEnum.py $alias1 $alias2 $alias3

# Usage Example 

![usage_screenshot](https://raw.githubusercontent.com/baybled/AliasEnum/main/example%20picture.png)

# Future

- split aliases of 2+ words, output shows 2+ word combos
- combos observe word symmetry (e.g. xx_little_lover_xx preserves xx at the start and end for new combos)
- combos observe pheonitic patterns (e.g. if all aliases are 3 syllables, combos must be 3 syllables)

# Troubleshooting

python3 must be located in /usr/bin/python3
