import matlab.engine
import gui_module  # 请确保这个模块的名称是正确的

parameters = gui_module.get_parameters()

eng = matlab.engine.start_matlab()

eng.storedata(parameters['iterations'],
              parameters['threshold'],
              parameters['lb'],
              parameters['ub'],
              parameters['theta1'],
              parameters['theta2'],
              parameters['theta3'],
              parameters['theta4'],
              parameters['delta_theta1_case1'],
              parameters['delta_theta2_case1'],
              parameters['delta_theta3_case1'],
              parameters['delta_theta4_case1'],
              parameters['delta_theta1_case2'],
              parameters['delta_theta2_case2'],
              parameters['delta_theta3_case2'],
              parameters['delta_theta4_case2'],
              parameters['a'],
              parameters['b'],
              parameters['c'],
              parameters['d'],
              )
