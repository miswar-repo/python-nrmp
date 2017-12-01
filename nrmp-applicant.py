'''
Author : Miswar
Based On The NRMP Match https://www.youtube.com/watch?v=kvgfgGmemdA
The NRM with Applicant Proposing First
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

programMatchs 	= {}
freeApplicant 	= []
checkApplicant  =copy.deepcopy(rankApplicant)

def matching(applicant):
	'''Find the free program available to a applicant '''
	print("Matching %s"%(applicant))

	rankApplicant[applicant] = list(checkApplicant[applicant])

	'''If Applicant not have program again, remove from free Applicant '''
	if(len(rankApplicant[applicant])==0):
		freeApplicant.remove(applicant)
		print('- Applicant %s not have program to check again '%(applicant))
					
	else:
		for program in rankApplicant[applicant]:
			
			#Cek whether program is full or not
			if len(programMatchs[program]) < positionProgram[program]:
				if applicant not in rankProgram[program]:
					print('- Applicant %s not exist in list applicant in program %s '%(applicant,program))
					checkApplicant[applicant].remove(program)
				else:	
					programMatchs[program].append(applicant)
					freeApplicant.remove(applicant)
					print('- %s is no longer a free applicant and is now tentatively get program %s'%(applicant, program))
					break
			else:
				print('- %s is full (%s participant) '%(program,positionProgram[program]))

				if applicant not in rankProgram[program]:
					print('- Applicant %s not exist in list applicant in program %s '%(applicant,program))
					checkApplicant[applicant].remove(program)
				else :
					# get applicant who can remove, 
					applicantRemove = applicant
					for applicantMatch in programMatchs[program]:
						if rankProgram[program].index(applicantRemove) < rankProgram[program].index(applicantMatch): 
							applicantRemove = applicantMatch

					if applicantRemove==applicant:
						print('- Rank Applicant %s in Program %s is bigger then other current applicant match '%(applicant,program))
						checkApplicant[applicant].remove(program)
					else:
						print('- %s is better than %s'%(applicant, applicantRemove))
						print('- Making %s free again.. and tentatively match %s and %s'%(applicantRemove, applicant, program))

						#The new applicant have match 
						freeApplicant.remove(applicant)
						programMatchs[program].append(applicant)

						#The old applicant is now not match anymore
						freeApplicant.append(applicantRemove)
						programMatchs[program].remove(applicantRemove)

						break

			

# init all applicant free and not have program
for applicant in rankApplicant.keys():
	freeApplicant.append(applicant)

# init programMatch
for program in rankProgram.keys():
	programMatchs[program]=[]

# Matching algorithm until stable match terminates
while (len(freeApplicant) > 0):
	for applicant in freeApplicant:
		matching(applicant)

print("\nMatching Done\n",programMatchs)

