import json
from abc import ABC, abstractmethod


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, file_name, data):
        pass


class SerialToJson(SerializationInterface):
    def serialize(self, file_name, data_json):
        with open(file_name, 'w', encoding='utf-8') as fh:
            json.dump(data_json, fh)

    def deserialize(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as fh:
            return json.load(fh)


class SerialToBin(SerializationInterface):
    def serialize(self, file_name, data):
        with open(file_name, 'wb') as fh:
            fh.write(data.encode())

    def deserialize(self, file_name):
        with open(file_name, 'rb') as fh:
            return fh.read().decode()


data_test = 'Python Web 6'

instance_bin = SerialToBin()
instance_json = SerialToJson()


instance_bin.serialize('test.bin', data_test)
instance_json.serialize('test.json', data_test)

print(instance_bin.deserialize('test.bin'))
print(instance_json.deserialize('test.json'))


# 2
class Meta(type):
    class_number = 0

    def __new__(mcs, name, bases, namespace, **kwargs):
        print(f'__new__ Meta {mcs.class_number}')
        instance = super().__new__(mcs, name, bases, namespace, **kwargs)
        instance.class_number = mcs.class_number
        mcs.class_number += 1
        mcs.children_number = mcs.class_number
        return instance


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)
    print(Meta.children_number)
