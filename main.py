#!/usr/bin/env python3

#TODO make menus align for all elements

from element import Element
import subprocess

#long names of each element
names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

#symbols to go with each element
symbols = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

atomicweight = [1.008, 4.003, 6.941, 9.012, 10.811, 12.011, 14.007, 15.999, 18.998, 20.180, 22.990, 24.305, 26.982, 28.086, 30.974, 32.065, 35.453, 39.948, 39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.390, 69.723, 72.640, 74.922, 78.960, 79.904, 83.800, 85.468, 87.620, 88.906, 91.224, 92.906, 95.940, 98.000, 101.070, 102.906, 106.420, 107.868, 112.411, 114.818, 118.710, 121.760, 127.600, 126.905, 131.293, 132.906, 137.327, 138.906, 140.116, 140.908, 144.240, 145.000, 150.360, 151.964, 157.250, 158.925, 162.500, 164.930, 167.259, 168.934, 173.040, 174.967, 178.490, 180.948, 183.840, 186.207, 190.230, 192.217, 195.078, 196.967, 200.590, 204.383, 207.200, 208.980, 209.000, 210.000, 222.000, 223.000, 226.000, 227.000, 232.038, 231.036, 238.029, 237.000, 244.000, 243.000, 247.000, 247.000, 251.000, 252.000, 257.000, 258.000, 259.000, 262.000, 261.000, 262.000, 266.000, 264.000, 277.000, 268.000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




#clear screen from input
def clearScreen():
    subprocess.call("clear",shell=True)

#initially empty list of elements
elements = []

#fill elements list
for i in range(0, 118):
    elements.append(Element(symbols[i], names[i], i + 1, atomicweight[i]))

#getting user input
def getInput():
    inputString = input(">> ").lower().strip()
    return inputString

#prints only first time
print("Enter an element name, symbol, or atomic number (not case sensitive)")
print("Type \"exit\" when finished")
print("Type \"clear\" to clear the screen")
#first input
inputString = getInput()
#keep going until one of these strings is reached
while inputString != "exit" and inputString != "end" and inputString != "done":
    #search symbols for matches
    for i in elements:
        #check for clearing screen keywords
        if (inputString == "clear" or
        inputString == "cls"):
            clearScreen()
        #if name, symbol, or atomic number matches
        elif (inputString == i.getName().lower() or
        inputString == i.getSymbol().lower()  or
        inputString == str(i.getAnum()).lower()):
            #print the match
            print(i.toString())
    #get the next input
    inputString = getInput()
