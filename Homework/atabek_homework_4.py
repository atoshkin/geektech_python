GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del GeekTech['bag']

GeekTech['address'] = "Ibraimova 103"

GeekTech["contacts"] = "+996-507-052-018"
GeekTech["instagram"] = "geektech__kg"

GeekTech['courses'].append("iOS")
GeekTech['courses'].append("IT English")
GeekTech['courses'].append("UX/UI")
GeekTech['courses'].append("GeekCamp")

GeekTech['courses'] = tuple(GeekTech['courses'])

for k, v in GeekTech.items():
    print(f"{k}: {v}")
    
print(GeekTech.keys())
print(GeekTech.values())