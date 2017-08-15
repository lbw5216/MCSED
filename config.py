""" MCSED - config.py


1) Configuration Settings

.. moduleauthor:: Greg Zeimann <gregz@astro.as.utexas.edu>

"""

# Fixed metallicity of SSP models
metallicity = 0.02

# SSP code for models
ssp = 'fsps' # 'fsps'
isochrone = 'padova' # 'padova', 'basti', 'mist', 'geneva', 'parsec'

# Dictionaries
metallicity_dict = {'padova':[0.0002,0.0003,0.0004,0.0005,0.0006,0.0008,
                              0.0010,0.0012,0.0016,0.0020,0.0025,0.0031,
                              0.0039,0.0049,0.0061,0.0077,0.0096,0.0120,
                              0.0150,0.0190,0.0240,0.0300]}
# Parameter ranges and fixed values

