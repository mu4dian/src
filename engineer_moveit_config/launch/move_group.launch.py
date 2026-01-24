from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("engineer", package_name="engineer_moveit_config")
        .to_moveit_configs()
    )
#----------------------新增参数内容----------------------
    # 关键：把 octomap 参数直接加到 move_group 参数命名空间
    # 注意：planning_scene_monitor() 现在的实现没有嵌套 namespace，所以这里直接放平
    moveit_config.planning_scene_monitor.update({
        "octomap_frame": "base_link",
        "octomap_resolution": 0.01, #这里可以调整八叉树分辨率
    })

    return generate_move_group_launch(moveit_config)
