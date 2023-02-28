from jinja2 import Template


bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id {{ router_id }} 
 bgp log-neighbor-changes
 neighbor {{ peer_1 }} remote-as 44

"""

my_template = bgp_config

j2_template = Template(my_template)
output = j2_template.render(bgp_as = 22, router_id = "1.1.1.1", peer_1 = "10.20.30.1")
print(output)
 
