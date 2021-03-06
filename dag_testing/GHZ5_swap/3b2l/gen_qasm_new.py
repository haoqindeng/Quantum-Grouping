from qiskit import *
from qiskit.compiler import transpile
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import *
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import dag_visualization
from qiskit.converters import circuit_to_dag
import os
from ctypes import c_int, addressof
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
import networkx.algorithms.isomorphism as iso
import xlrd  #引入模块

right_gate = 0
test_gate = 0

temp = []

all_results = []

latency_table = []

# workbook=xlrd.open_workbook("../latency_list_mapped/qasm_list_24.csv.xlsx")  #文件路径
# worksheet=workbook.sheet_by_index(0)
# nrows=worksheet.nrows  #获取该表总行数
# for i in range(nrows): #循环打印每一行
#     latency_table.append(worksheet.row_values(i)[0])  #以列表形式读出，列表中的每一项是str类型

one_gate_latency_list = ['cx', 't', 'tdg', 'x', 'rz', 'h']
one_gate_latency_dict = {}
one_gate_latency_dict['cx'] = 5.78125
one_gate_latency_dict['t'] = 4.21875
one_gate_latency_dict['h'] = 3.90625
one_gate_latency_dict['tdg'] = 3.90625
one_gate_latency_dict['x'] = 3.90625
one_gate_latency_dict['rz'] = 4.21875

# IBMQ.load_account()
dist_table = []

dist_table_dict = {}

dist_file_dict = {}

qasm_table = []

right_gates = 0		
test_gates = 0

basedir = '/home/haoqindeng/Desktop/Quantum-Grouping/dag_testing/swapped_qasm'
filename_list = os.listdir(basedir)
for item in filename_list:
    path=os.path.join(basedir,item)
    file=os.path.splitext(item)
    filename,typen=file
    if typen == '.qasm':
        parentPath = '../../swapped_qasm/'
        parentPath = parentPath + filename + typen
        print(parentPath)

        ghz = QuantumCircuit.from_qasm_file(parentPath)
        
        # device = IBMQ.get_backend('ibmq_16_melbourne')

        # trans_ghz = transpile(ghz, device)

        dag = circuit_to_dag(ghz)

        # dag_drawer(dag, scale=0.7, filename='../pic/alu-v2_31.png')

        dag_id_depth = {}

        idDict = {} # _node_id to dag_id(starting from 0)

        idDict2 = {} # _dag_id to inDegreeList_id(starting from 0)

        groupResult = []

        groupQargs = {}

        dagList = []

        one_gate_list = []

        # dag_id to group index:
        id_group_index_dict = {}

        swap_gate_list = []

        groupIndex_to_distIndex = {}

        inDegreeList = []
        l1 = []
        l2 = []
        l3 = []
        inDegreeList.append(l1)
        inDegreeList.append(l2)
        inDegreeList.append(l3)

        print("inDegreeList's length is: " + str(len(inDegreeList)))

        # mark depth:


        # 0:nd, 1:inDegree, 2:counter, 3:qargs, 4:successorList, 5:predecessorList

        counter = 0
        for nd in dag.topological_nodes():
            inDegree = len(list(dag.predecessors(nd)))
            successorList = list(dag.successors(nd)).copy()
            predecessorList = list(dag.predecessors(nd)).copy()
            nodeType = nd.type
            tempList = [nd, inDegree, counter, nd.qargs, successorList, predecessorList, nodeType]
            # update inDegreeList
            copyList = inDegreeList[inDegree]
            copyList.append(tempList)
            # update dagList
            dagList.append(tempList.copy())
            # update idDict
            idDict[nd._node_id] = counter
            # update idDict2
            index = len(copyList) - 1
            item = [inDegree, index]
            idDict2[counter] = item

            counter += 1

            right_gate += 1

        print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        counter = 0
        for nd in dagList:
            # print(str(counter) + " " + nd[0].name + " " + str(nd[1]) )
            if (nd[0].type == 'op'):		
                right_gates += 1
            counter += 1
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        # node(new_node) that has 
        # [0:nd, 1:inDegree, 2:counter(dagID), 3:qargs(list of qarg), 4:successorList(of DagNodes), 5:predecessorList(of DagNodes), 6:type]
        # rename nodes into rz, x, y, z, h, s, sdg, t, tdg
        name_dict = {}
        name_dict[0] = 'rz'
        name_dict[1] = 'x'
        name_dict[2] = 'y'
        name_dict[3] = 'z'
        name_dict[4] = 'h'
        name_dict[5] = 's'
        name_dict[6] = 'sdg'
        name_dict[7] = 't'
        name_dict[8] = 'tdg'
        counter = 0
        for nd in dag.topological_nodes():
            # print(counter, end = ' ')
            if nd.name == 'u1':
                num = int(nd.op.params[0])
                # print(num)
                # if (num <= 0):
                #     new_name = 'rz'
                # else:
                new_name = name_dict[num]
                nd.name = new_name
            counter += 1


        for nd in dagList:
            if nd[6] != 'op':
                continue
            dag_id = nd[2]
            pred_list = nd[5]
            max_depth = 0
            for pred in pred_list:
                if pred.type != 'op':
                    continue
                pred_node_id = pred._node_id
                pred_dag_id = idDict[pred_node_id]
                if dag_id_depth[pred_dag_id] > max_depth:
                    max_depth = dag_id_depth[pred_dag_id]              
            dag_id_depth[dag_id] = max_depth + 1

        # counter = 0
        # for nd in dag.topological_nodes():
        #     if nd.type == 'op':
        #         nd.name = nd.name + ' ' + str(counter) + ' ' + str(dag_id_depth[counter])
        #     else:
        #         nd.name = nd.name + ' ' + str(counter)
        #     counter += 1

        # dag_drawer(dag, scale=0.8, filename='v3.png')


       
            # counter = 0
            # for ls in inDegreeList:
            #     iterator = 0
            #     for sls in ls:
            #         print(str(counter) + " " + sls[0].name + " " + str(sls[1]) + " " + str(sls[2]) + " ", end = " " )
            #         print("qargs: ", end = " ")
            #         for qargs in sls[3]:
            #             print(str(qargs[1]), end = " ")
            #         print("sucessors: ", end = " ")
            #         for succ in sls[4]:
            #             print(succ.name + " " + str(succ._node_id), end = " ")
            #         print("predecessors: ", end = " ")
            #         for pred in sls[5]:
            #             print(pred.name + " " + str(pred._node_id), end = " ")
            #         print("position is: " + str(iterator), end = " ")
            #         print (sls[6])
            #         iterator += 1
            #     counter += 1

        print("******************************************")
        print("|||||||||||||all the tests are done|||||||")
        print("|||||||||||||now starts|||||||||||||||||||")
        print("******************************************")
        # for ls in inDegreeList:
        #     # subList stores a list of tempList/nodeObj = [nd, inDegree, counter, nd.qargs, successorList]
        #     for subList in ls:

        # stores the list of node obj with incoming degree 0
        zeroList = inDegreeList[0]

        # zeroList contains node(new_node) that has [0:nd, 1:inDegree, 2:counter(dagID), 3:qargs(list of qarg), 4:successorList(of DagNodes), 5:predecessorList(of DagNodes), 6:type]
        iterator = 0
        while iterator < len(dagList):
            
            node = zeroList[iterator]
            # prejudge swap:
            if node[0].name == 'swap':
                temp_list = [node[2]]
                groupResult.append(temp_list)
                swap_gate_list.append(node[2])

                index = len(groupResult) - 1  
                # update groupQargs
                bitSet = set()
                for qarg in node[3]:
                    bitSet.add(qarg[1])
                groupQargs[index] = bitSet
            else:
                # print(str(iterator) + " " + str(node[2]), end = " ")
                predNodeList = node[5]
                indexList = []
                # for each predecessor:
                for predNode in predNodeList:
                    # if predNode.name == 'swap':
                    #     continue
                    dagID = idDict[predNode._node_id]
                    index = 0
                    # based on dagID, iterate groupResult to find connected components
                    while index < len(groupResult):
                        # if dagID belongs to a parent group
                        if dagID in groupResult[index]:
                            indexList.append(index)
                            break
                        index += 1
                # print("correct until line 127", end = " ")
                new_group = False
                one_swap_parent = False
                swap_parent = -1
                if len(indexList) == 1:
                    if groupResult[indexList[0]][0] in swap_gate_list:
                        new_group = True
                elif len(indexList) == 2:
                    index1 = indexList[0]
                    index2 = indexList[1]
                    if groupResult[index1][0] in swap_gate_list and groupResult[index2][0] in swap_gate_list:
                        new_group = True
                    elif groupResult[index1][0] in swap_gate_list and groupResult[index2][0] not in swap_gate_list:
                        one_swap_parent = True
                        swap_parent = index2
                    elif groupResult[index1][0] not in swap_gate_list and groupResult[index2][0] in swap_gate_list:
                        one_swap_parent = True
                        swap_parent = index1
                # if node[2] == 7:
                #     print(str(node[2]) + ' ' + str(one_swap_parent) )
                #     print(indexList)
                #     print(groupResult[indexList[0]])
                #     print(groupResult[indexList[1]])
                #     print(groupResult)
                #     print(swap_gate_list)
                if len(indexList) == 0 or new_group == True:
                    # only if it is op!!!
                    # if node[0].type == 'op':
                    newList = []
                    newList.append(node[2])
                    groupResult.append(newList)
                    index = len(groupResult) - 1  
                    # update groupQargs
                    bitSet = set()
                    for qarg in node[3]:
                        bitSet.add(qarg[1])
                    groupQargs[index] = bitSet
                elif len(indexList) == 1 or one_swap_parent == True:
                    

                    if len(indexList) == 1:
                        index1 = indexList[0]
                        # if one_swap_parent == True:
                        #     index1 = swap_parent
                        copyList = groupResult[index1]
                        copyList.append(node[2])
                        # update groupQargs
                        bitSet = set()
                        for qarg in node[3]:
                            bitSet.add(qarg[1])
                        groupQargs[index1] = groupQargs[index1].union(bitSet)
                    else:
                        index1 = indexList[0]
                        index2 = indexList[1]
                        bitSet = set()
                        for qarg in node[3]:
                            bitSet.add(qarg[1])
                        copyGroup1 = groupQargs[index1].copy()
                        copyGroup2 = groupQargs[index2].copy()
                        totalGroup = copyGroup1.union(copyGroup2)
                        totalGroup = totalGroup.union(bitSet)
                        if len(totalGroup) < 2:
                            index1 = swap_parent
                            copyList = groupResult[index1]
                            copyList.append(node[2])
                            # update groupQargs
                            bitSet = set()
                            for qarg in node[3]:
                                bitSet.add(qarg[1])
                            groupQargs[index1] = groupQargs[index1].union(bitSet)
                        else:
                            newList = []
                            newList.append(node[2])
                            groupResult.append(newList)
                            index = len(groupResult) - 1  
                            # update groupQargs
                            bitSet = set()
                            for qarg in node[3]:
                                bitSet.add(qarg[1])
                            groupQargs[index] = bitSet

                else: # len(indexList) == 2
                    index1 = indexList[0]
                    index2 = indexList[1]
                    if (index1 == index2): # belong to the same group
                        copyList = groupResult[index1]
                        copyList.append(node[2])
                    else: # belong to different groups
                        # check whether exceeds 2 bits
                        bitSet = set()
                        for qarg in node[3]:
                            bitSet.add(qarg[1])
                        # print(str(node[2]) + ' ' + str(one_swap_parent), end = ' ')
                        # print(indexList, end = ' ')
                        # print(len(groupResult))
                        copyGroup1 = groupQargs[index1].copy()
                        copyGroup2 = groupQargs[index2].copy()
                        totalGroup = copyGroup1.union(copyGroup2)
                        totalGroup = totalGroup.union(bitSet)
                        # if not exceeds 2 bits
                        if len(totalGroup) <= 3:
                            # merge two group, discard index2   groupResult:[[dagid1, dagid2, dagid3.....],[],[]...] groupQargs:{{0, 1},{},{}...}
                            newList = []
                            newList.append(node[2])
                            totalList = groupResult[index1] + groupResult[index2] + newList
                            groupResult[index1] = totalList.copy()
                            groupResult[index2].clear()
                            groupQargs[index1] = totalGroup
                            groupQargs[index2] = set()
                        # if exceeds 3 bits
                        else:
                            copyGroup1 = copyGroup1.union(bitSet)
                            copyGroup2 = copyGroup2.union(bitSet)
                            if len(copyGroup1) <= 3 and len(copyGroup2) <= 3: # arbitrarily choose group1
                                copyList = groupResult[index1]
                                copyList.append(node[2])
                                # update groupQargs
                                bitSet = set()
                                for qarg in node[3]:
                                    bitSet.add(qarg[1])
                                groupQargs[index1] = groupQargs[index1].union(bitSet)
                            elif len(copyGroup1) <= 3 and len(copyGroup2) > 3:
                                copyList = groupResult[index1]
                                copyList.append(node[2])
                                # update groupQargs
                                bitSet = set()
                                for qarg in node[3]:
                                    bitSet.add(qarg[1])
                                groupQargs[index1] = groupQargs[index1].union(bitSet)
                            elif len(copyGroup2) <= 3 and len(copyGroup1) > 3:
                                copyList = groupResult[index2]
                                copyList.append(node[2])
                                # update groupQargs
                                bitSet = set()
                                for qarg in node[3]:
                                    bitSet.add(qarg[1])
                                groupQargs[index2] = groupQargs[index2].union(bitSet)
                            else: # cannot be grouped into either parent parent, start a new group
                                newList = []
                                newList.append(node[2])
                                groupResult.append(newList)
                                index = len(groupResult) - 1
                                # update groupQargs
                                bitSet = set()
                                for qarg in node[3]:
                                    bitSet.add(qarg[1])
                                groupQargs[index] = bitSet
            iterator += 1  
            # print("number of succNode: " + str(len(node[4])), end = " ")
            # now updating incoming degree of successors
            for succNode in node[4]:
                succNodeId = succNode._node_id
                succNodeDagId = idDict[succNodeId]
                # print("succNodeDagId is: " + str(succNodeDagId), end = " ")
                newSuccNode = dagList[succNodeDagId].copy()
              
                succNodeInDegreeId = idDict2[succNodeDagId]
                # move the successor to the list of inDegree - 1
                # first remove it from list of inDegree
                inDegree = succNodeInDegreeId[0]
                index = succNodeInDegreeId[1]
                copyList = inDegreeList[inDegree]
            
                copyList[index].clear()
                # second add it to list of inDegree - 1
                inDegree = succNodeInDegreeId[0] - 1
                copyList2 = inDegreeList[inDegree]
                copyList2.append(newSuccNode)  
               
                index = len(copyList2) - 1
                newPos = [inDegree, index]
                idDict2[succNodeDagId] = newPos
                # print("new pos:", end = " ")
                # print(newPos, end = " ")
                # print("succNode position: " + str(inDegree) + " " + str(index), end = " ")
              
            # print("next: ", end = " ")
            # print(zeroList[0])
            # print()
            
        print(swap_gate_list)
        print(groupResult)

        # eliminate non-op gates

        newGroupResult = []

        for group in groupResult:
            newGroup = []
            for dagID in group:
                if dagList[dagID][6] == 'op':
                    newGroup.append(dagID)
            if len(newGroup) > 0:
                newGroupResult.append(newGroup)

        print(newGroupResult)

        # partition groups

        id_depth_dict = {} # stores dagID->depth

        # node(new_node) that has 
        # [0:nd, 1:inDegree, 2:counter(dagID), 3:qargs(list of qarg), 4:successorList(of DagNodes), 5:predecessorList(of DagNodes), 6:type]

        # it = 0
        # for group in newGroupResult:

        #     first_dag_id = group[0]
        #     first_depth = dag_id_depth[first_dag_id]
        #     for dag_id in group:
        #         id_depth_dict[dag_id] = dag_id_depth[dag_id] - first_depth + 1

        #     # iterator = 1
        #     # while iterator < len(group):
        #     #     # print(iterator, end = ' ')
        #     #     dag_id = group[iterator]
        #     #     node = dagList[dag_id]
        #     #     pred_list = node[5] 
        #     #     deepest_depth = 1
        #     #     # add restriction to pred to only op, also to already detected
        #     #     for pred in pred_list:
        #     #         if (pred.type != 'op'):
        #     #             continue
        #     #         pred_node_id = pred._node_id
        #     #         pred_dag_id = idDict[pred_node_id]
        #     #         # print('pred_dag_id is: ' + str(pred_dag_id), end = ' ')
        #     #         if pred_dag_id not in id_depth_dict:
        #     #             continue
        #     #         depth = id_depth_dict[pred_dag_id] + 1
        #     #         if depth > deepest_depth:
        #     #             deepest_depth = depth
        #     #     id_depth_dict[dag_id] = deepest_depth
        #     #     iterator += 1        
        #     it += 1
           
        # print(id_depth_dict)
        # id_depth_dict.clear()

        finalGroupingResult = []

        # divide depth

        for group in newGroupResult:
            depth_id_dict = {}
            max_depth = 0
            for dag_id in group:
                depth = dag_id_depth[dag_id]
                if depth > max_depth:
                    max_depth = depth
                if depth in depth_id_dict:
                    depth_id_dict[depth].append(dag_id)  
                else:
                    new_list = []
                    new_list.append(dag_id)
                    depth_id_dict[depth] = new_list
            
            # first_dag_id = group[0]
            # first_depth = dag_id_depth[first_dag_id]
            shallowest_depth = 100000
            for dag_id in group:
                depth = dag_id_depth[dag_id]
                if depth < shallowest_depth:
                    shallowest_depth = depth    

            layer = 0
            iter_depth = shallowest_depth
            while iter_depth <= max_depth:
                if iter_depth > max_depth:
                    break
                sub_group = []
                layer = 1
                while 1 == 1:
                    if layer > 3:
                        break
                    if iter_depth > max_depth:
                        break
                    if iter_depth in depth_id_dict:
                        sub_group = sub_group + depth_id_dict[iter_depth]
                        layer += 1
                    else:
                        iter_depth += 1
                        break
                    iter_depth += 1
                if len(sub_group) > 0:
                    finalGroupingResult.append(sub_group)
            
            # iterator = 0
            # depth_id_dict = {}
            # for dag_id in group:
            #     depth = int((id_depth_dict[dag_id] + 1) / 2)
            #     if depth in depth_id_dict:
            #         depth_id_dict[depth].append(dag_id)
            #     else:
            #         new_list = []
            #         new_list.append(dag_id)
            #         depth_id_dict[depth] = new_list
            # layer = 1
            
            # for layer in depth_id_dict:
            #     list_copy = depth_id_dict[layer].copy()
            #     finalGroupingResult.append(list_copy)
               
        print(finalGroupingResult)    
        # print(id_depth_dict)
        it = 0
        for group in finalGroupingResult:
            test_gate += 1
            # print(it, end = ': ')
            first_dag_id = group[0]
            id_depth_dict[first_dag_id] = 1
            iterator = 1
            while iterator < len(group):
                # print(iterator, end = ' ')
                dag_id = group[iterator]
                node = dagList[dag_id]
                pred_list = node[5] 
                deepest_depth = 1
                # add restriction to pred to only op, also to already detected
                for pred in pred_list:
                    if (pred.type != 'op'):
                        continue
                    pred_node_id = pred._node_id
                    pred_dag_id = idDict[pred_node_id]
                    # print('pred_dag_id is: ' + str(pred_dag_id), end = ' ')
                    if pred_dag_id not in id_depth_dict:
                        continue
                    if pred_dag_id not in group:
                        continue
                    depth = id_depth_dict[pred_dag_id] + 1
                    if depth > deepest_depth:
                        deepest_depth = depth
                id_depth_dict[dag_id] = deepest_depth
                iterator += 1        
            it += 1
       
        print(id_depth_dict)
        # the format of subgraph: list1: [[0:dag_id, 1:name, 2:[q1, q2]], []], list2: []

        # node(new_node) that has 
        # [0:nd, 1:inDegree, 2:counter(dagID), 3:qargs(list of qarg), 4:successorList(of DagNodes), 5:predecessorList(of DagNodes), 6:type]

        
        group_index = -1
        # turn the group into networkx graph
        for group in finalGroupingResult:
            group_index += 1
            if len(group) <= 1:
                if dagList[group[0]][0].name != 'swap':
                    one_gate_list.append(group[0])
                    continue
            # reassign qarg values
            qarg_dict = {}
            value_index = 1
            for dag_id in group:
                node = dagList[dag_id]
                qargs = node[3]
                for qarg in qargs:
                    if qarg[1] not in qarg_dict:
                        qarg_dict[qarg[1]] = value_index
                        value_index += 1 
                        
            G = nx.Graph()
            G.clear()
            dumb_node = 'Z'
            qasm = ''
            for dag_id in group: # # map each dag_id to group_index
                
                if id_depth_dict[dag_id] % 3 == 1: # if on the first level
                    node = dagList[dag_id]
                    name = node[0].name + '_' + str(dag_id)
                    gate_name = node[0].name # for qasm
                    qasm = qasm + gate_name + " " # for qasm
                    G.add_nodes_from([name], fill=node[0].name)
                    qargs = node[3]
                    i = 0
                    for qarg in qargs:
                        new_qarg = qarg_dict[qarg[1]]
                        qasm = qasm + 'q[' + str(new_qarg) + ']' # for qasm
                        if len(qargs) > 1 and i == 0: # for qasm
                            qasm = qasm + ',' # for qasm
                        else: # for qasm
                            qasm = qasm + ';\n' # for qasm
    
                        G.add_nodes_from([dumb_node], fill='dumb')
                        G.add_weighted_edges_from([(dumb_node, name, new_qarg)])
                        dumb_node = chr(ord(dumb_node) - 1)
                        i += 1
                else: # if on the second level:
                    node = dagList[dag_id]
                    name = node[0].name + '_' + str(dag_id)
                    gate_name = node[0].name # for qasm
                    qasm = qasm + gate_name + ' ' # for qasm
                    G.add_nodes_from([name], fill=node[0].name)
                    qargs = node[3]
                    pred_list = node[5]
                    index = 0
                    i = 0
                    for qarg in qargs:
                        new_qarg = qarg_dict[qarg[1]]
                        qasm = qasm + 'q[' + str(new_qarg) + ']' # for qasm
                        if len(qargs) > 1 and i == 0: # for qasm
                            qasm = qasm + ',' # for qasm
                        else: # for qasm
                            qasm = qasm + ';\n' # for qasm
                        if index >= len(pred_list):
                            continue
                        pred = pred_list[index]
                        pred_node_id = pred._node_id
                        pred_dag_id = idDict[pred_node_id]
                        pred_node = dagList[pred_dag_id]
                        pred_node_name = pred_node[0].name + '_' + str(pred_dag_id)
                        if pred_dag_id in group: # if in the group, connect them
                            G.add_weighted_edges_from([(name, pred_node_name, new_qarg)])
                        else: # if not in the group connect it to a dumb_node
                            G.add_nodes_from([dumb_node], fill='dumb')
                            G.add_weighted_edges_from([(dumb_node, name, new_qarg)]) 
                            dumb_node = chr(ord(dumb_node) - 1)
                        index += 1 
                        i += 1
            # compare with known structures in table_list
        
            em = iso.numerical_edge_match('weight', 1)
            nm = iso.categorical_node_match('fill', 'dumb')
            
            index = 0
            found = False
            while index < len(dist_table):
                H = dist_table[index]
                if nx.is_isomorphic(G, H, node_match=nm, edge_match=em):
                    dist_table_dict[index] = dist_table_dict[index] + 1
                    found = True
                    # map group_index to dist_index
                    groupIndex_to_distIndex[group_index] = index
                    break
                index += 1
            if not found: # add a new structure
                dist_table.append(G)
                pos = len(dist_table) - 1
                dist_table_dict[pos] = 1

                dist_file_dict[pos] = parentPath

                qasm_table.append(qasm)
                # map group_index to dist_index
                groupIndex_to_distIndex[group_index] = pos

        for group in finalGroupingResult:		
            for dag_id in group:		
                test_gates += 1


iterator = 0
while iterator < len(dist_table):
    G = dist_table[iterator]
    suffix = str(iterator)
    file_name = 'structures/structure_' + suffix
    edge_labels=dict([((u,v,),d['weight'])
                for u,v,d in G.edges(data=True)])
    pos = nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx(G, pos)
    plt.savefig(file_name)
    plt.clf()
    iterator += 1

print(dist_table_dict)

print(dist_file_dict)


i = 0
output = open('qasm_3b3l.txt', 'w')
for qasm in qasm_table:
    output.write(str(i) + ':\n')
    output.write(qasm)
    i += 1
output.close()

print(right_gates)		
print(test_gates)

#         group_index = 0
#         for group in finalGroupingResult:
#             for dag_id in group:
#                 id_group_index_dict[dag_id] = group_index
#             group_index += 1

#         # print(id_group_index_dict)


#         # node(new_node) that has 
#         # [0:nd, 1:inDegree, 2:counter(dagID), 3:qargs(list of qarg), 4:successorList(of DagNodes), 5:predecessorList(of DagNodes), 6:type]

#         max_latency_table = [] # keep track of max_latency
#         i = 0
#         while i < len(dagList):
#             max_latency_table.append(0)
#             i += 1

#         for nd in dagList:
#             if nd[6] != 'op':
#                 continue
#             dag_id = nd[2]
#             group_index = id_group_index_dict[dag_id]
#             group = finalGroupingResult[group_index]
        
#             max_latency = 0
#             pred_list = nd[5]

#             invalid_predecessor = True
#             within_group = True
#             for pred in pred_list:
#                 to_continue1 = True
#                 to_continue2 = True
#                 pred_node_id = pred._node_id
#                 pred_dag_id = idDict[pred_node_id]
                
#                 if pred_dag_id in group:
#                     to_continue1 = False
#                 else:
#                     within_group = False
#                 if pred.type != 'op':
#                     to_continue2 = False
#                 else:
#                     invalid_predecessor = False
#                 if to_continue1 == False or to_continue2 == False:
#                     continue        
#                 pred_group_index = id_group_index_dict[pred_dag_id]
#                 if max_latency_table[pred_group_index] > max_latency:
#                     max_latency = max_latency_table[pred_group_index]
#             current_latency = 0
#             if dag_id not in one_gate_list:
#                 dist_index = groupIndex_to_distIndex[group_index]
#                 current_latency = latency_table[dist_index]
#             else:
#                 gate_name = dagList[dag_id][0].name
#                 current_latency = one_gate_latency_dict[gate_name]

#             if within_group == False and invalid_predecessor == False:
#                 max_latency_table[group_index] = max_latency + current_latency 
#             elif within_group == False and invalid_predecessor == True:
#                 max_latency_table[group_index] = current_latency 
#             elif within_group == True:
#                 max_latency_table[group_index] = max_latency_table[group_index]

#         print(max_latency_table)

#         max_lat = 0
#         for lat in max_latency_table:
#             if lat > max_lat:
#                 max_lat = lat

#         # all_results.append(max_lat)

#         # original latency
#         original_latency_table = []
#         i = 0
#         while i < len(dagList):
#             original_latency_table.append(0)
#             i += 1

#         for nd in dagList:
#             if nd[6] != 'op':
#                 continue
#             dag_id = nd[2]
#             gate_name = nd[0].name  

#             max_latency = 0
#             pred_list = nd[5]
#             for pred in pred_list:
#                 if pred.type != 'op':
#                     continue
#                 pred_node_id = pred._node_id
#                 pred_dag_id = idDict[pred_node_id]
#                 if original_latency_table[pred_dag_id] > max_latency:
#                     max_latency = original_latency_table[pred_dag_id]              
#             original_latency_table[dag_id] = max_latency + one_gate_latency_dict[gate_name]

#         print(original_latency_table)

#         org_lat = 0
#         for lat in original_latency_table:
#             if lat > org_lat:
#                 org_lat = lat

#         print(str(max_lat) + ' ' + str(org_lat))
#         all_results.append(max_lat / org_lat)


# print(all_results)

# print(groupIndex_to_distIndex)

# #one_gate_latency_list = ['cx', 't', 'tdg', 'x', 'rz', 'h']
# one_gate_latency_dict = {}
# one_gate_latency_dict['cx'] = 5.78125
# one_gate_latency_dict['t'] = 4.21875
# one_gate_latency_dict['h'] = 3.90625
# one_gate_latency_dict['tdg'] = 3.90625
# one_gate_latency_dict['x'] = 3.90625
# one_gate_latency_dict['rz'] = 4.21875
