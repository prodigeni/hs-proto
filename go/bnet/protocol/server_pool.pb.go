// Code generated by protoc-gen-go.
// source: bnet/protocol/server_pool.proto
// DO NOT EDIT!

/*
Package bnet_protocol_server_pool is a generated protocol buffer package.

It is generated from these files:
	bnet/protocol/server_pool.proto

It has these top-level messages:
	GetLoadRequest
	PoolStateRequest
	ServerState
	ServerInfo
	PoolStateResponse
*/
package bnet_protocol_server_pool

import proto "github.com/golang/protobuf/proto"
import math "math"
import bnet_protocol "bnet"
import bnet_protocol_attribute "bnet/protocol"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = math.Inf

type GetLoadRequest struct {
	XXX_unrecognized []byte `json:"-"`
}

func (m *GetLoadRequest) Reset()         { *m = GetLoadRequest{} }
func (m *GetLoadRequest) String() string { return proto.CompactTextString(m) }
func (*GetLoadRequest) ProtoMessage()    {}

type PoolStateRequest struct {
	XXX_unrecognized []byte `json:"-"`
}

func (m *PoolStateRequest) Reset()         { *m = PoolStateRequest{} }
func (m *PoolStateRequest) String() string { return proto.CompactTextString(m) }
func (*PoolStateRequest) ProtoMessage()    {}

type ServerState struct {
	CurrentLoad      *float32 `protobuf:"fixed32,1,opt,name=current_load,def=1" json:"current_load,omitempty"`
	GameCount        *uint32  `protobuf:"varint,2,opt,name=game_count" json:"game_count,omitempty"`
	PlayerCount      *uint32  `protobuf:"varint,3,opt,name=player_count" json:"player_count,omitempty"`
	XXX_unrecognized []byte   `json:"-"`
}

func (m *ServerState) Reset()         { *m = ServerState{} }
func (m *ServerState) String() string { return proto.CompactTextString(m) }
func (*ServerState) ProtoMessage()    {}

const Default_ServerState_CurrentLoad float32 = 1

func (m *ServerState) GetCurrentLoad() float32 {
	if m != nil && m.CurrentLoad != nil {
		return *m.CurrentLoad
	}
	return Default_ServerState_CurrentLoad
}

func (m *ServerState) GetGameCount() uint32 {
	if m != nil && m.GameCount != nil {
		return *m.GameCount
	}
	return 0
}

func (m *ServerState) GetPlayerCount() uint32 {
	if m != nil && m.PlayerCount != nil {
		return *m.PlayerCount
	}
	return 0
}

type ServerInfo struct {
	Host             *bnet_protocol.ProcessId             `protobuf:"bytes,1,opt,name=host" json:"host,omitempty"`
	Replace          *bool                                `protobuf:"varint,2,opt,name=replace" json:"replace,omitempty"`
	State            *ServerState                         `protobuf:"bytes,3,opt,name=state" json:"state,omitempty"`
	Attribute        []*bnet_protocol_attribute.Attribute `protobuf:"bytes,4,rep,name=attribute" json:"attribute,omitempty"`
	ProgramId        *uint32                              `protobuf:"fixed32,5,opt,name=program_id" json:"program_id,omitempty"`
	XXX_unrecognized []byte                               `json:"-"`
}

func (m *ServerInfo) Reset()         { *m = ServerInfo{} }
func (m *ServerInfo) String() string { return proto.CompactTextString(m) }
func (*ServerInfo) ProtoMessage()    {}

func (m *ServerInfo) GetHost() *bnet_protocol.ProcessId {
	if m != nil {
		return m.Host
	}
	return nil
}

func (m *ServerInfo) GetReplace() bool {
	if m != nil && m.Replace != nil {
		return *m.Replace
	}
	return false
}

func (m *ServerInfo) GetState() *ServerState {
	if m != nil {
		return m.State
	}
	return nil
}

func (m *ServerInfo) GetAttribute() []*bnet_protocol_attribute.Attribute {
	if m != nil {
		return m.Attribute
	}
	return nil
}

func (m *ServerInfo) GetProgramId() uint32 {
	if m != nil && m.ProgramId != nil {
		return *m.ProgramId
	}
	return 0
}

type PoolStateResponse struct {
	Info             []*ServerInfo `protobuf:"bytes,1,rep,name=info" json:"info,omitempty"`
	XXX_unrecognized []byte        `json:"-"`
}

func (m *PoolStateResponse) Reset()         { *m = PoolStateResponse{} }
func (m *PoolStateResponse) String() string { return proto.CompactTextString(m) }
func (*PoolStateResponse) ProtoMessage()    {}

func (m *PoolStateResponse) GetInfo() []*ServerInfo {
	if m != nil {
		return m.Info
	}
	return nil
}

func init() {
}
