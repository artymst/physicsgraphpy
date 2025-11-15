import matplotlib.pyplot as plt

def plot_all(motion, color_position='blue', color_velocity='green', color_acceleration='red'):
    plt.figure(figsize=(10,6))
    plt.subplot(3,1,1)
    plt.plot(motion.times, motion.positions, color=color_position)
    plt.title('Position vs Time')
    plt.ylabel('Position (m)')

    plt.subplot(3,1,2)
    plt.plot(motion.times, motion.velocities, color=color_velocity)
    plt.title('Velocity vs Time')
    plt.ylabel('Velocity (m/s)')

    plt.subplot(3,1,3)
    plt.plot(motion.times, motion.get_accelerations(), color=color_acceleration)
    plt.title('Acceleration vs Time')
    plt.ylabel('Acceleration (m/s^2)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()

def plot_projectile(proj, color='purple'):
    plt.plot(proj.xs, proj.ys, color=color)
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.title("Projectile Motion")
    plt.show()

def animate_motion(motion):
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_xlim(0, max(motion.times))
    ax.set_ylim(min(motion.positions), max(motion.positions))

    def update(frame):
        line.set_data(motion.times[:frame], motion.positions[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(motion.times), blit=True)
    plt.show()
