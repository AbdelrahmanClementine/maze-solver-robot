from controller import Robot


robot = Robot()
timestep = int(robot.getBasicTimeStep())
max_speed = 6.28

left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

prox_sensors = []
for ind in range(8):
    sensor = robot.getDistanceSensor(f'ps{ind}')
    sensor.enable(timestep)
    prox_sensors.append(sensor)

while robot.step(timestep) != -1:

    sensor_values = [sensor.getValue() for sensor in prox_sensors]
    
    left_wall = sensor_values[5] > 80
    left_corner = sensor_values[6] > 80
    front_wall = sensor_values[7] > 200  

    if front_wall:
        # left_motor.setVelocity(-0.5 * max_speed)
        # right_motor.setVelocity(-0.5 * max_speed)
        # robot.step(timestep * 5)

        left_motor.setVelocity(1.0 * max_speed)
        right_motor.setVelocity(-1.0 * max_speed)
        robot.step(timestep * 5)
    elif left_wall:
    
        left_motor.setVelocity(0.5 * max_speed)
        right_motor.setVelocity(0.5 * max_speed)
    else:
        left_motor.setVelocity(0.25 * max_speed)
        right_motor.setVelocity(0.5 * max_speed)

    if left_corner:
        left_motor.setVelocity(0.5 * max_speed)
        right_motor.setVelocity(0.3 * max_speed)

    for i, val in enumerate(sensor_values):
        print(f"Sensor[{i}] = {val:.2f}")
