'''
Author : Miswar
Based On The NRMP Match https://www.youtube.com/watch?v=kvgfgGmemdA
The NRM with Program Proposing First
'''

import collections
import copy

rankApplicant = {
	'Arthur': 	['City'],
	'Sunny': 	['City', 'Mercy'],
	'Joseph':  	['City', 'General', 'Mercy'],
	'Latha':	['Mercy', 'City', 'General'],
	'Darrius':	['City', 'Mercy', 'General'],
}

rankProgram = {
	'Mercy': 	['Darrius', 'Joseph'],
	'City': 	['Darrius', 'Arthur', 'Sunny', 'Latha','Joseph'],
	'General': 	['Darrius', 'Arthur', 'Joseph', 'Latha'],
	
}

positionProgram = {
	'Mercy'		: 2,
	'City'		: 2,
	'General'	: 2,
}


applicantMatchs 	= {}
freeProgram 		= []
checkProgram 	 	=copy.deepcopy(rankProgram)
 

def matching(program):
	'''Find the free applicant available to a program '''
	print("Matching %s"%(program))
	
	rankProgram[program] = list(checkProgram[program])
	
	'''If program not have applicant and slot again, remove from free Program '''

	if(len(rankProgram[program])==0 or positionProgram[program] < 1):
		freeProgram.remove(program)
		print('- Program %s not have applicant to check or not have slot again '%(program))
					
	else:
		for applicant in rankProgram[program]:
			
			#Cek whether applicant is taken or not
			if applicantMatchs[applicant] == "":
				if program not in rankApplicant[applicant]:
					print('- Program %s not exist in list program in applicant %s '%(program,applicant))
					checkProgram[program].remove(applicant)
				else:	
					applicantMatchs[applicant]=program
					positionProgram[program]-= 1

					print('- %s is now tentatively get applicant %s '%(program, applicant))
					break
			else:
				print('- %s is already get program %s '%(applicant,applicantMatchs[applicant]))

				if program not in rankApplicant[applicant]:
					print('- Program %s not exist in list program in applicant %s '%(program,applicant))
					checkProgram[program].remove(applicant)

				else :
					# get program who can remove, 
					if rankApplicant[applicant].index(applicantMatchs[applicant]) < rankApplicant[applicant].index(program): 
						print('- Rank Program %s in Applicant %s is bigger then current program %s  '%(program,applicant,applicantMatchs[applicant]))
						checkProgram[program].remove(applicant)
					else:
						print('- %s is better than %s'%(program, applicantMatchs[applicant]))
						print('- Making %s free again.. and tentatively match %s and %s'%(applicantMatchs[applicant], program, applicant))

						#The old program is now not match anymore
						positionProgram[applicantMatchs[applicant]] += 1
						checkProgram[applicantMatchs[applicant]].remove(applicant)
						freeProgram.append(applicantMatchs[applicant])
						
						#The new applicant have match 
						applicantMatchs[applicant]=program
						positionProgram[program]-=1
						
						break

			

# init all applicant free and not have program
for program in rankProgram.keys():
	freeProgram.append(program)

# init applicantMatchs
for applicant in rankApplicant.keys():
	applicantMatchs[applicant]=""

# Matching algorithm until stable match terminates
i=1
while (len(freeProgram) > 0 ):
	for program in freeProgram:
		matching(program)
		i=i+1
		

print("\nMatching Done\n",applicantMatchs)

