# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateHybridClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'CreateHybridCluster','ehs')

	def get_VolumeProtocol(self):
		return self.get_query_params().get('VolumeProtocol')

	def set_VolumeProtocol(self,VolumeProtocol):
		self.add_query_param('VolumeProtocol',VolumeProtocol)

	def get_OsTag(self):
		return self.get_query_params().get('OsTag')

	def set_OsTag(self,OsTag):
		self.add_query_param('OsTag',OsTag)

	def get_RemoteDirectory(self):
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self,RemoteDirectory):
		self.add_query_param('RemoteDirectory',RemoteDirectory)

	def get_EhpcVersion(self):
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self,EhpcVersion):
		self.add_query_param('EhpcVersion',EhpcVersion)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_SecurityGroupName(self):
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self,SecurityGroupName):
		self.add_query_param('SecurityGroupName',SecurityGroupName)

	def get_EcsOrderComputeInstanceType(self):
		return self.get_query_params().get('EcsOrder.Compute.InstanceType')

	def set_EcsOrderComputeInstanceType(self,EcsOrderComputeInstanceType):
		self.add_query_param('EcsOrder.Compute.InstanceType',EcsOrderComputeInstanceType)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_VolumeType(self):
		return self.get_query_params().get('VolumeType')

	def set_VolumeType(self,VolumeType):
		self.add_query_param('VolumeType',VolumeType)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_Nodes(self):
		return self.get_query_params().get('Nodes')

	def set_Nodes(self,Nodes):
		self.add_query_param('Nodes',Nodes)

	def get_Applications(self):
		return self.get_query_params().get('Applications')

	def set_Applications(self,Applications):
		for i in range(len(Applications)):	
			if Applications[i].get('Tag') is not None:
				self.add_query_param('Application.' + str(i + 1) + '.Tag' , Applications[i].get('Tag'))


	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_VolumeId(self):
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self,VolumeId):
		self.add_query_param('VolumeId',VolumeId)

	def get_VolumeMountpoint(self):
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self,VolumeMountpoint):
		self.add_query_param('VolumeMountpoint',VolumeMountpoint)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)