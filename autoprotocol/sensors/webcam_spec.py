from sensors import webcam

camera = webcam(pins = {...},...)

camera.on()                              # turn on camera
camera.off()                             # turn off camera
camera.record()                          # starts recording
camera.record(30)                        # records for 30 minutes
camera.record(30, post = True)           # records for 30 minutes push to server when done

camera.capture()                         # takes photo
camera.capture(2, 10, post = True)       # takes 2 photos every 10 minutes push to server when done
camera.stop()                            # stops recording




