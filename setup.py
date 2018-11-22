from cx_Freeze import setup,Executable

setup(name='HospitalAppointment',
      version ='1.0',
      description = 'Hospital appointment', executables = [Executable("appointment.py")], requires=['pyttsx3'])