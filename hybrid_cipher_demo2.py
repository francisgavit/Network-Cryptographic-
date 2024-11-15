# -*- coding: utf-8 -*-
"""Hybrid_Cipher_Demo2.ipynb

Automatically generated by Colaboratory.


# PROJECT 

# **CRPTOGRAPHY SYSTEM USING VIGENERE CIPHER AND POLYBIUS CIPHER**

### By- PARMESWAR
"""

#Hello
#How's you ?
#This Hybrid Cipher is developed for Communication security for Army, Secure high level Communication, Message and Data Protection from attackers


# Python code to implement Cryptographic System 
# First Step is to Give Input to the System

# System 1 : Vigenere Cipher 

# This function generates the 
# key in a cyclic manner until 
# it's length isn't equal to 
# the length of original text 
def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key))


