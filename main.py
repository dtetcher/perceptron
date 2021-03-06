from concrete.perceptron import Perceptron
from concrete.activation import Threshold


def main():
    input_data = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    training_speed = 0.2

    p = Perceptron(input_data=input_data,
                   output_layer_pattern=lambda x: x[0] and (not x[1] or x[2]),
                   activation_function=Threshold(),
                   training_speed=training_speed,
                   stuck_condition=True
                   )

    p.load()

    p.begin_training(laps=200_000)
    # p.dump()


if __name__ == '__main__':
    main()
