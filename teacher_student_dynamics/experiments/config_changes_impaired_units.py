import itertools

param_config_changes = {
    f"param_{h}_{f}_{s}": [
        {"networks": {"student_hidden": h, "teacher_hidden": h}},
        {"training": {"freeze_units": [f, 0]}},
        {"curriculum": {"switch_steps": [s]}},
    ]
    for h, f, s in itertools.product(
        [1, 2, 4], [1, 2, 3, 4], [1000, 10000, 100000, 1000000, 10000000]
    )
}
oparam_config_changes = {
    f"oparam_{h}_{f}_{s}": [
        {"networks": {"student_hidden": 2 * h, "teacher_hidden": h}},
        {"training": {"freeze_units": [f, 0]}},
        {"curriculum": {"switch_steps": [s]}},
    ]
    for h, f, s in itertools.product(
        [1, 2, 4], [1, 2, 3, 4], [1000, 10000, 100000, 1000000, 10000000]
    )
}
CONFIG_CHANGES = {**param_config_changes, **oparam_config_changes}
