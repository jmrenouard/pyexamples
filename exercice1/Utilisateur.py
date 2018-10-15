#!/usr/bin/python3

class Utilisateur:
	def __init__(self, prenom, nom):
		self.prenom = prenom
		self.nom = nom
	def qui_est_tu(self):
		print("Je suis %s %s" % (self.prenom, self.nom))
if __name__ == '__main__':
	napoleon=Utilisateur('Napoleon', 'Bonaparte')
	napoleon.qui_est_tu()


