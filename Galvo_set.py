
import PyDAQmx

value_X = -0.18
value_Y = -0.63

task_X = PyDAQmx.Task()
task_Y = PyDAQmx.Task()

task_X.CreateAOVoltageChan("/Dev1/ao0","",
                   -10.0,10.0,PyDAQmx.DAQmx_Val_Volts,None)
task_Y.CreateAOVoltageChan("/Dev1/ao1","",
                   -10.0,10.0,PyDAQmx.DAQmx_Val_Volts,None)

task_X.StartTask()
task_Y.StartTask()

task_X.WriteAnalogScalarF64(0,10.0,value_X,None)
task_Y.WriteAnalogScalarF64(1,10.0,value_Y,None)

task_X.StopTask()
task_Y.StopTask()