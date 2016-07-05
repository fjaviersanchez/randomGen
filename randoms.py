def make_hp_map(nside,data_name):
    import healpy as hp
    import astropy.table as tab
    import numpy as np
    data = tab.Table.read(data_name)
    pix_nums = hp.ang2pix(nside,np.pi/2-data['dec']*np.pi/180,data['ra']*np.pi/180)
    bin_count = np.bincount(pix_nums)
    map_gal = np.append(bin_count,np.zeros(12*nside**2-len(bin_count)))
    return map_gal

def make_random(nside,data,Nf,outfile=None,viewmap=True,fmt='ascii',rsd=True):
    import healpy as hp
    import numpy as np
    import astropy.table as tab
    import matplotlib.pyplot as plt
    data_tab = tab.Table.read(data)
    ran=np.hstack((data_tab,)*Nf)
    Nr=len(ran)
    ran['ra']=np.random.uniform(0,360,Nr)
    ran['dec']=np.degrees(np.arcsin(np.random.uniform(-1,1,Nr)))
    map_gal = make_hp_map(nside,data)
    pix_nums = hp.ang2pix(nside,np.pi/2-ran['dec']*np.pi/180,ran['ra']*np.pi/180)
    mask = map_gal[pix_nums]>0
    if(rsd):
        new_random = tab.Table([ran['ra'][mask],ran['dec'][mask],ran['z'][mask]+ran['dz'][mask],np.ones(len(ran['ra'][mask]))],names=('ra','dec','z','w'))
    else:
        new_random = tab.Table([ran['ra'][mask],ran['dec'][mask],ran['z'][mask],np.ones(len(ran['ra'][mask]))],names=('ra','dec','z','w'))
    if(outfile!=None):
        new_random.write(outfile,format=fmt)
    if(viewmap):
        pix_nums = hp.ang2pix(nside,np.pi/2-new_random['dec']*np.pi/180,new_random['ra']*np.pi/180)
        bin_count = np.bincount(pix_nums)
        map_ran = np.append(bin_count,np.zeros(12*nside**2-len(bin_count)))
        plt.figure()
        hp.mollview(map_ran)
    return ran
