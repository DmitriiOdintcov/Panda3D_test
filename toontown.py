import imports
import database as db

db.maps.extend({'filename' : "phase_15/hood/toontown_central.bam"})
db.actors.extend([
                {'filename_body' : "phase_3.5/models/char/suit3-mod.bam",
                 'animations' : {'fingerwag' : "phase_5/models/char/suit3-finger-wag.bam"},
                 'filename_head' : "phase_4/models/char/suitB-heads.bam",
                 'headname' : "loanshark",
                 'filename_texture_torso' : "phase_3.5/maps/m_blazer.jpg",
                 'filename_texture_arm' : "phase_3.5/maps/m_sleeve.jpg",
                 'filename_texture_leg' : "phase_3.5/maps/m_leg.jpg",
                 'position' : [10, 4, 90],}
                 ])

db.initialise('maps', 0)

db.initialise('actors', 0)
db.actors[0].loop('fingerwag')


base.oobe()
run()