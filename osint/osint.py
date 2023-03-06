
import whois
import sys

domain_name = sys.argv[1]

whoisSearch = whois.whois(domain_name)


print("# Informations sur le nom de domaine #")
print("Nom de domaine :", whoisSearch.domain_name)

print("\n# Informations Whois #")
print("\nRegistrar :", whoisSearch.registrar)
print("\n Nom des serveurs :", whoisSearch.name_servers)
print("\n Date de création:", whoisSearch.creation_date)
print("\n Date mise à jour:", whoisSearch.updated_date)
print("\n Date d'expiration:", whoisSearch.expiration_date)


print("\n# Informations sur le propriétaire#")
print("Nom du propriétaire :", whoisSearch.name)
print("\n emails du propriétaire :", whoisSearch.emails)
print("\n Organisation :", whoisSearch.organization)
print("\n Pays:", whoisSearch.country)
