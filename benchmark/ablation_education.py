import json
import os.path

from benchmark.benchmark_class import BenchmarkTest, run_agent_on_benchmark
from benchmark.benchmark_file_util import make_dir_for_benchmark
from person.action.brain_qwen.qwen import QWen
from person.action.brain_chat_glm.chat_glm import ChatGLM2
from person.action.brain_xverse.xverse import XVerse
from person.action.brain_vicuna.vicuna import Vicuna
from person.action.brain.agent import Agent
from util.education import education_list, education_full_name_list
from util.file_util import load_json_file

ROOT_PATH = "/home/location2/pycharm/GPTMan/db/benchmark"
benchmark_root = f"{ROOT_PATH}/{{benchmark_type}}/{{person_name}}/profile_v1/system_v1/benchmark_v2"
benchmark_gold_answer_file = f"{benchmark_root}/questions.json"
benchmark_root_path = f"{benchmark_root}/{{prompt_kind}}/"


def make_dirs_and_files():
    # make dirs
    for name in education_list:
        new_name = "homer_education_" + name
        for prompt_kind in ["few_shot", "zero_shot"]:
            for benchmark_type in ["basic_information", "role_non_relation", "role_relation"]:
                make_dir_for_benchmark(benchmark_type=benchmark_type, person_name=new_name, prompt_kind=prompt_kind,
                                       benchmark_version="benchmark_v2", profile_version="profile_v1",
                                       system_version="system_v1")

    # copy gold answer file
    for name in education_list:
        new_name = "homer_education_" + name
        for benchmark_type in ['basic_information', "role_non_relation", "role_relation"]:
            origin_gold_answer_file = f"/home/location2/pycharm/GPTMan/db/benchmark/{benchmark_type}/homer/profile_v1/system_v1/benchmark_v2/questions.json"
            target_gold_answer_file = f"/home/location2/pycharm/GPTMan/db/benchmark/{benchmark_type}/{new_name}/profile_v1/system_v1/benchmark_v2/questions.json"
            origin_file_obj = load_json_file(origin_gold_answer_file)
            origin_file_str = json.dumps(origin_file_obj)
            new_file_str = origin_file_str.replace("Springfield High School(graduated)", name)

            with open(target_gold_answer_file, "w") as f:
                f.write(new_file_str)

    # make benchmark files empty {}
    for name in education_list:
        new_name = "homer_education_" + name
        for benchmark_type in ['basic_information', "role_non_relation", "role_relation"]:
            for prompt_kind in ["few_shot", "zero_shot"]:
                target_path = f"/home/location2/pycharm/GPTMan/db/benchmark/{benchmark_type}/{new_name}/profile_v1/system_v1/benchmark_v2/{prompt_kind}/prompt1.json"
                with open(target_path, "w") as f:
                    f.write("{}")


def copy_anthropomorphize():
    root_path = f"/home/location2/pycharm/GPTMan/db/template/{{new_name}}/examples_and_requirements/"
    # make dirs
    for name in education_list:
        new_name = "homer_education_" + name
        path_ = root_path.format(new_name=new_name)
        if not os.path.exists(path_):
            os.makedirs(path_)

    # copy anthropomorphize file
    for name in education_list:
        new_name = "homer_education_" + name
        origin_file = f"{root_path.format(new_name='homer')}/anthropomorphize.json"
        target_file = f"{root_path.format(new_name=new_name)}/anthropomorphize.json"
        origin_file_obj = load_json_file(origin_file)
        origin_file_str = json.dumps(origin_file_obj)
        """new_file_str = origin_file_str.replace("simpson", name.lower())
        new_file_str = new_file_str.replace("Simpson", name)"""
        with open(target_file, "w") as f:
            f.write(origin_file_str)


if __name__ == "__main__":
    # 'Qwen-14B-Chat', "Qwen-7B-Chat" done
    # 'chatglm2-6b-32k', "chatglm2-6b" done
    # "XVERSE-13B-Chat" done
    # "vicuna-7b-v1.5-16k" done
    # longchat-7b-32k-v1.5 done
    # longchat-13b-16k done
    # longchat-7b-16k done
    # vicuna-13b-v1.5-16k done
    for model_name in ["gpt-3.5-turbo-16k", "gpt-4"]:
        for person_name in ["homer_education_" + name for name in education_list]:
            prompt_name = "prompt1"
            profile_version = "profile_v1"
            system_version = "system_v1"
            benchmark_version = "benchmark_v2"
            batch_size = 1
            time_sleep = 1
            if model_name == 'gpt-3.5-turbo-16k':
                batch_size = 1
            elif model_name == 'gpt-4':
                batch_size = 1
            agent = Agent(profile_version=profile_version,
                           system_version=system_version,
                           person_name=person_name,
                           model_name=model_name,
                           )
            run_agent_on_benchmark(
                person_name, prompt_name, profile_version, system_version, benchmark_version, batch_size, agent,
                time_sleep=time_sleep,zero_shot=False)
    """make_dirs_and_files()
    copy_anthropomorphize()"""
