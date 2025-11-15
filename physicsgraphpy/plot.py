import matplotlib.pyplot as plt

def plot_all(motion):
    plt.figure(figsize=(10,6))
    plt.subplot(3,1,1)
    plt.plot(motion.times, motion.positions)
    plt.title('Position vs Time')
    plt.ylabel('Position (m)')

    plt.subplot(3,1,2)
    plt.plot(motion.times, motion.velocities)
    plt.title('Velocity vs Time')
    plt.ylabel('Velocity (m/s)')

    plt.subplot(3,1,3)
    plt.plot(motion.times, motion.get_accelerations())
    plt.title('Acceleration vs Time')
    plt.ylabel('Acceleration (m/s^2)')
    plt.xlabel('Time (s)')

    plt.tight_layout()
    plt.show()
