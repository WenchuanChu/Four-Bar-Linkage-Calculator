import matlab.engine

# 启动 MATLAB session
eng = matlab.engine.start_matlab()

# 调用 MATLAB 函数
results = eng.get_optimized_results()

# 打印结果
for row in results:
    print([round(item, 3) for item in row])

# 关闭 MATLAB session
eng.quit()