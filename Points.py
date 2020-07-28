import pandas as pd
import numpy as np
import math
# df = pd.read_csv("data.csv")
# co = 0
#
# test_points = pd.DataFrame(df, columns=['test_point'])
# tes = np.zeros_like(test_points)
#
# 对于一道题的得分，计算为（最终得分*0.95^(本题提交次数-1)），最低扣到原来的70%为止。
# for i in range(0, len(df) - 1):
#     if df.iloc[i]["final_score"] == 0:
#         tes[i][0] = 0
#     else:
#         if df.iloc[i]["user_id"] == df.iloc[i + 1]["user_id"] and df.iloc[i]["case_id"] == df.iloc[i + 1]["case_id"] and \
#                 df.iloc[i]["score"] != 100:
#             co += 1
#             tes[i][0] = (df.iloc[i]["final_score"]) * pow(0.95, co) if pow(0.95, co) >= 0.7 else (df.iloc[i][
#                 "final_score"]) * 0.7
#         else:
#             tes[i][0] = (df.iloc[i]["final_score"]) * pow(0.95, co) if pow(0.95, co) >= 0.7 else (df.iloc[i][
#                 "final_score"]) * 0.7
#             co = 0
#
# df.insert(7, 'test_point', tes)
# df.to_csv("new_data3.csv")
#
# 去重
#
# ddf = pd.read_csv("new_data3.csv")
# pdd = ddf.drop_duplicates(subset=["user_id", "case_id"], keep="last", inplace=False)
# pdd.to_csv("new_data3.csv", index=None)
#
# 综合计算
#
# dddf = pd.read_csv("new_data3.csv")
# co_linerlist = 0
# linerlist_point = 0
# co_string = 0
# string_point = 0
# co_array = 0
# array_point = 0
# co_sort = 0
# sort_point = 0
# co_graph = 0
# graph_point = 0
# co_tree = 0
# tree_point = 0
# co_find = 0
# find_point = 0
# co_num = 0
# num_point = 0
# overPoints = pd.DataFrame(dddf, columns=['over_point'])
# ov = np.zeros_like(overPoints)
# current_id = dddf.iloc[0]["user_id"]
# for i in range(len(dddf)):
#     if current_id == dddf.iloc[i]["user_id"]:
#         if dddf.iloc[i]["case_type"] == "线性表":
#             co_linerlist += 1
#             linerlist_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = linerlist_point / co_linerlist
#         elif dddf.iloc[i]["case_type"] == "数组":
#             co_array += 1
#             array_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = array_point / co_array
#         elif dddf.iloc[i]["case_type"] == "字符串":
#             co_string += 1
#             string_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = string_point / co_string
#         elif dddf.iloc[i]["case_type"] == "查找算法":
#             co_find += 1
#             find_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = find_point / co_find
#         elif dddf.iloc[i]["case_type"] == "排序算法":
#             co_sort += 1
#             sort_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = sort_point / co_sort
#         elif dddf.iloc[i]["case_type"] == "数字操作":
#             co_num += 1
#             num_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = num_point / co_num
#         elif dddf.iloc[i]["case_type"] == "树结构":
#             co_tree += 1
#             tree_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = tree_point / co_tree
#         elif dddf.iloc[i]["case_type"] == "图结构":
#             co_graph += 1
#             graph_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = graph_point / co_graph
#     else:
#         co_linerlist = 0
#         linerlist_point = 0
#         co_string = 0
#         string_point = 0
#         co_array = 0
#         array_point = 0
#         co_sort = 0
#         sort_point = 0
#         co_graph = 0
#         graph_point = 0
#         co_tree = 0
#         tree_point = 0
#         co_find = 0
#         find_point = 0
#         co_num = 0
#         num_point = 0
#         current_id = dddf.iloc[i]["user_id"]
#         if dddf.iloc[i]["case_type"] == "线性表":
#             co_linerlist += 1
#             linerlist_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = linerlist_point / co_linerlist
#         elif dddf.iloc[i]["case_type"] == "数组":
#             co_array += 1
#             array_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = array_point / co_array
#         elif dddf.iloc[i]["case_type"] == "字符串":
#             co_string += 1
#             string_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = string_point / co_string
#         elif dddf.iloc[i]["case_type"] == "查找算法":
#             co_find += 1
#             find_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = find_point / co_find
#         elif dddf.iloc[i]["case_type"] == "排序算法":
#             co_sort += 1
#             sort_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = sort_point / co_sort
#         elif dddf.iloc[i]["case_type"] == "数字操作":
#             co_num += 1
#             num_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = num_point / co_num
#         elif dddf.iloc[i]["case_type"] == "树结构":
#             co_tree += 1
#             tree_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = tree_point / co_tree
#         elif dddf.iloc[i]["case_type"] == "图结构":
#             co_graph += 1
#             graph_point += dddf.iloc[i]["test_point"]
#             ov[i][0] = graph_point / co_graph
# dddf.insert(8, "over_point", ov)
# pddd = dddf.drop_duplicates(subset=["case_type", "user_id"], keep="last", inplace=False)
# pddd.to_csv("fin_data.csv", index=None)
# 排序 同时对所作的模块数目进行匹配，八个模块全做的设置all_done为1 否则为0
# pf = pd.read_csv("fin_data.csv")
# sort_points = pd.DataFrame(pf, columns=['sort_point'])
# sp = np.zeros_like(sort_points)
# current_id = pf.iloc[0]["user_id"]
# all_done = pd.DataFrame(pf, columns=['all_done'])
# ad = np.zeros_like(all_done)
# point_sum = 0
# coo = 0
# for i in range(len(pf)):
#     if current_id == pf.iloc[i]["user_id"]:
#         coo += 1
#         point_sum += pf.iloc[i]["over_point"]
#         sp[i][0] = point_sum
#         if coo == 7:
#             ad[i][0] = 1
#     else:
#         current_id = pf.iloc[i]["user_id"]
#         coo = 0
#         point_sum = 0
#         point_sum += pf.iloc[i]["over_point"]
#         sp[i][0] = point_sum
# pf.insert(9, "sort_point", sp)
# pf.insert(10, "all_done", ad)
# ppf = pf.drop_duplicates(subset=["user_id"], keep="last", inplace=False)
# ppf = ppf.sort_values(by=['sort_point'], ascending=False, inplace=False)
# ppf.to_csv("final_pre_data.csv")
print(math.log(0.7,0.95))
