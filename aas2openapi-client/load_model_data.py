import pandas
from aas2openapi_client.client import Client
from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_quality_data_get import sync as qualitysync
from aas2openapi_client.models.process_data import *
from aas2openapi_client.models.new_values_machine_parameter import *
from aas2openapi_client.models.machine_parameter import *
from aas2openapi_client.models.new_values_process_data import *
from aas2openapi_client.models.quality_feature import *
from typing import List
from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_resource_get import sync as resource_sync
from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_procedure_get import sync as procedure_sync

def load_quality_results(data: List[QualityFeature]):
    i = 0
    j = 0
    list_final = []

    while i < len(data[j].result.new_results):
        quality_value_list = []
        quality_value_list.append(data[j].result.new_results[i].part_counter)
        while j < len(data):
            if data[0].result.new_results[i].part_counter == data[j].result.new_results[i].part_counter:
                quality_value_list.append(data[j].result.new_results[i].value)
                j += 1
            else:
                j += 1
        j = 0
        i += 1
        list_final.append(quality_value_list.copy())
    return list_final


def load_quality_keys(data: List[QualityFeature]):
    j = 0
    final_list = []
    quality_value_list = []
    quality_value_list.append('part_counter')
    while j < len(data):
        quality_value_list.append(data[j].feature_type)
        j += 1
    final_list.append(quality_value_list)
    return final_list


def load_process_data(data: List[NewValuesProcessData]):
    i = 0
    j = 0
    final_list = []

    while i < len(data):
        list_process_data = []
        list_process_data.append(data[i].timestamp)
        while j < len(data[i].values):
            list_process_data.append(data[i].values[j])
            j += 1
        i += 1
        final_list.append(list_process_data.copy())
    return final_list


def load_process_keys(data: ProcessData):
    j = 0
    final_list = []
    list_process_data = []
    list_process_data.append('timestamp')
    while j < len(data.features_list):
        list_process_data.append(data.features_list[j])
        j += 1
    final_list.append(list_process_data.copy())
    return final_list


def load_machine_data(data: List[NewValuesMachineParameter]):
    i = 0
    j = 0
    final_list = []

    while i < len(data):
        list_process_data = []
        list_process_data.append(data[i].timestamp)
        while j < len(data[i].value):
            list_process_data.append(data[i].value[j])
            j += 1
        i += 1
        final_list.append(list_process_data.copy())
    return final_list


def load_machine_data_keys(data: MachineParameter):
    i = 0
    final_list = []
    list_keys = []
    list_keys.append('timestamp')
    while i < len(data):
        list_keys.append(data[i].value_description)
        i += 1
    final_list.append(list_keys.copy())
    return final_list


# partcounter zeit aus production_times zuordnen, ggfs Funktion die Qualitätsdaten Anlagenparameter und Processdaten zuordnet


client = Client(base_url="http://127.0.0.1:8000")
quality_data = qualitysync(item_id="12string", client=client)
procedure = procedure_sync(item_id="12string", client=client)
resource = resource_sync(item_id="12string", client=client)

procedure_loaded = load_process_data(procedure.process_data.new_values)
loaded = load_quality_results(quality_data.quality_feature)
machine_loaded = load_machine_data(resource.new_machine_parameter.new_values_machine_parameter)

df = pandas.DataFrame(loaded)
df.columns = load_quality_keys(quality_data.quality_feature)
print(df)

df2 = pandas.DataFrame(procedure_loaded)
df2.columns = load_process_keys(procedure.process_data)
print(df2)

df3 = pandas.DataFrame(machine_loaded)
df3.columns = load_machine_data_keys(resource.machine_parameter)
print(df3)


data_dict = {
    'value_' + str(quality_data.quality_feature[0].feature_type): [value.value for value in quality_data.quality_feature[0].result.new_results],
    'part_counter': [part.part_counter for part in quality_data.quality_feature[0].result.new_results],
    # 'feature_type': [feature.feature_type for feature in quality_data.quality_feature],
}
