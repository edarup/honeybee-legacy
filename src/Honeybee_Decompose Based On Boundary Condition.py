# By Mostapha Sadeghipour Roudsari
# Sadeghipour@gmail.com
# Honeybee started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

"""
Decompose zone surfaces by boundary condition
-
Provided by Honeybee 0.0.53

    Args:
        _HBZone: Honeybee Zone
        
    Returns:
        outdoors: A list of surfaces which has outdoors boundary condition
        surface: A list of surfaces which has surface boundary condition
        adiabatic: A list of surfaces which has adiabatic boundary condition
        ground: A list of surfaces which has ground boundary condition
"""
ghenv.Component.Name = "Honeybee_Decompose Based On Boundary Condition"
ghenv.Component.NickName = 'decomposeByBC'
ghenv.Component.Message = 'VER 0.0.53\nAUG_12_2014'
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "00 | Honeybee"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass


import scriptcontext as sc



def main(HBZone):
    # import the classes
    if not sc.sticky.has_key('honeybee_release'):
        print "You should first let Honeybee to fly..."
        w = gh.GH_RuntimeMessageLevel.Warning
        ghenv.Component.AddRuntimeMessage(w, "You should first let Honeybee to fly...")
        return
    
    outdoors = []
    surface = []
    adiabatic = []
    ground = []

    # call the objects from the lib
    hb_hive = sc.sticky["honeybee_Hive"]()

    zone = hb_hive.callFromHoneybeeHive([HBZone])[0]

    for srf in zone.surfaces:
        if srf.BC.lower() == "outdoors":
            if srf.hasChild:
                outdoors.append(srf.punchedGeometry)
                for childSrf in srf.childSrfs:
                    outdoors.append(childSrf.geometry)
            else:
                outdoors.append(srf.geometry)
        elif srf.BC.lower() == "surface":
            if srf.hasChild:
                surface.append(srf.punchedGeometry)
                for childSrf in srf.childSrfs:
                    surface.append(childSrf.geometry)
            else:
                surface.append(srf.geometry)
        elif srf.BC.lower() == "adiabatic":
            if srf.hasChild:
                adiabatic.append(srf.punchedGeometry)
                for childSrf in srf.childSrfs:
                    adiabatic.append(childSrf.geometry)
            else:
                adiabatic.append(srf.geometry)
        elif srf.BC.lower() == "ground":
            ground.append(srf.geometry)
        
    return outdoors, surface, adiabatic, ground


#    # add to the hive
#    hb_hive = sc.sticky["honeybee_Hive"]()
#    HBSurface  = hb_hive.addToHoneybeeHive(HBSurfaces, ghenv.Component.InstanceGuid.ToString() + str(uuid.uuid4()))

if _HBZone!= None:
    HBSurfaces = main(_HBZone)
    
    if HBSurfaces:
        outdoors = HBSurfaces[0]
        surface = HBSurfaces[1]
        adiabatic = HBSurfaces[2]
        ground = HBSurfaces[3]