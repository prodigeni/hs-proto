// Code generated by protoc-gen-go.
// source: SpectatorProto.proto
// DO NOT EDIT!

/*
Package SpectatorProto is a generated protocol buffer package.

It is generated from these files:
	SpectatorProto.proto

It has these top-level messages:
	JoinInfo
	Invite
	PartyServerInfo
*/
package SpectatorProto

import proto "github.com/golang/protobuf/proto"
import math "math"
import PegasusShared "."

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = math.Inf

type Constants int32

const (
	Constants_DEFAULT_PORT Constants = 3724
)

var Constants_name = map[int32]string{
	3724: "DEFAULT_PORT",
}
var Constants_value = map[string]int32{
	"DEFAULT_PORT": 3724,
}

func (x Constants) Enum() *Constants {
	p := new(Constants)
	*p = x
	return p
}
func (x Constants) String() string {
	return proto.EnumName(Constants_name, int32(x))
}
func (x *Constants) UnmarshalJSON(data []byte) error {
	value, err := proto.UnmarshalJSONEnum(Constants_value, data, "Constants")
	if err != nil {
		return err
	}
	*x = Constants(value)
	return nil
}

type JoinInfo struct {
	ServerIpAddress      *string                 `protobuf:"bytes,1,opt,name=server_ip_address" json:"server_ip_address,omitempty"`
	ServerPort           *uint32                 `protobuf:"varint,2,opt,name=server_port" json:"server_port,omitempty"`
	GameHandle           *int32                  `protobuf:"varint,3,opt,name=game_handle" json:"game_handle,omitempty"`
	SecretKey            *string                 `protobuf:"bytes,4,opt,name=secret_key" json:"secret_key,omitempty"`
	IsJoinable           *bool                   `protobuf:"varint,5,opt,name=is_joinable" json:"is_joinable,omitempty"`
	CurrentNumSpectators *int32                  `protobuf:"varint,6,opt,name=current_num_spectators" json:"current_num_spectators,omitempty"`
	MaxNumSpectators     *int32                  `protobuf:"varint,7,opt,name=max_num_spectators" json:"max_num_spectators,omitempty"`
	GameType             *PegasusShared.GameType `protobuf:"varint,8,opt,name=game_type,enum=PegasusShared.GameType" json:"game_type,omitempty"`
	MissionId            *int32                  `protobuf:"varint,9,opt,name=mission_id" json:"mission_id,omitempty"`
	SpectatedPlayers     []*PegasusShared.BnetId `protobuf:"bytes,10,rep,name=spectated_players" json:"spectated_players,omitempty"`
	PartyId              *PegasusShared.BnetId   `protobuf:"bytes,11,opt,name=party_id" json:"party_id,omitempty"`
	XXX_unrecognized     []byte                  `json:"-"`
}

func (m *JoinInfo) Reset()         { *m = JoinInfo{} }
func (m *JoinInfo) String() string { return proto.CompactTextString(m) }
func (*JoinInfo) ProtoMessage()    {}

func (m *JoinInfo) GetServerIpAddress() string {
	if m != nil && m.ServerIpAddress != nil {
		return *m.ServerIpAddress
	}
	return ""
}

func (m *JoinInfo) GetServerPort() uint32 {
	if m != nil && m.ServerPort != nil {
		return *m.ServerPort
	}
	return 0
}

func (m *JoinInfo) GetGameHandle() int32 {
	if m != nil && m.GameHandle != nil {
		return *m.GameHandle
	}
	return 0
}

func (m *JoinInfo) GetSecretKey() string {
	if m != nil && m.SecretKey != nil {
		return *m.SecretKey
	}
	return ""
}

func (m *JoinInfo) GetIsJoinable() bool {
	if m != nil && m.IsJoinable != nil {
		return *m.IsJoinable
	}
	return false
}

func (m *JoinInfo) GetCurrentNumSpectators() int32 {
	if m != nil && m.CurrentNumSpectators != nil {
		return *m.CurrentNumSpectators
	}
	return 0
}

func (m *JoinInfo) GetMaxNumSpectators() int32 {
	if m != nil && m.MaxNumSpectators != nil {
		return *m.MaxNumSpectators
	}
	return 0
}

func (m *JoinInfo) GetGameType() PegasusShared.GameType {
	if m != nil && m.GameType != nil {
		return *m.GameType
	}
	return PegasusShared.GameType_GT_UNKNOWN
}

func (m *JoinInfo) GetMissionId() int32 {
	if m != nil && m.MissionId != nil {
		return *m.MissionId
	}
	return 0
}

func (m *JoinInfo) GetSpectatedPlayers() []*PegasusShared.BnetId {
	if m != nil {
		return m.SpectatedPlayers
	}
	return nil
}

func (m *JoinInfo) GetPartyId() *PegasusShared.BnetId {
	if m != nil {
		return m.PartyId
	}
	return nil
}

type Invite struct {
	InviterGameAccountId *PegasusShared.BnetId `protobuf:"bytes,1,opt,name=inviterGameAccountId" json:"inviterGameAccountId,omitempty"`
	JoinInfo             *JoinInfo             `protobuf:"bytes,2,opt,name=join_info" json:"join_info,omitempty"`
	XXX_unrecognized     []byte                `json:"-"`
}

func (m *Invite) Reset()         { *m = Invite{} }
func (m *Invite) String() string { return proto.CompactTextString(m) }
func (*Invite) ProtoMessage()    {}

func (m *Invite) GetInviterGameAccountId() *PegasusShared.BnetId {
	if m != nil {
		return m.InviterGameAccountId
	}
	return nil
}

func (m *Invite) GetJoinInfo() *JoinInfo {
	if m != nil {
		return m.JoinInfo
	}
	return nil
}

type PartyServerInfo struct {
	ServerIpAddress  *string                 `protobuf:"bytes,1,opt,name=server_ip_address" json:"server_ip_address,omitempty"`
	ServerPort       *uint32                 `protobuf:"varint,2,opt,name=server_port" json:"server_port,omitempty"`
	GameHandle       *int32                  `protobuf:"varint,3,opt,name=game_handle" json:"game_handle,omitempty"`
	SecretKey        *string                 `protobuf:"bytes,4,opt,name=secret_key" json:"secret_key,omitempty"`
	GameType         *PegasusShared.GameType `protobuf:"varint,5,opt,name=game_type,enum=PegasusShared.GameType" json:"game_type,omitempty"`
	MissionId        *int32                  `protobuf:"varint,6,opt,name=mission_id" json:"mission_id,omitempty"`
	XXX_unrecognized []byte                  `json:"-"`
}

func (m *PartyServerInfo) Reset()         { *m = PartyServerInfo{} }
func (m *PartyServerInfo) String() string { return proto.CompactTextString(m) }
func (*PartyServerInfo) ProtoMessage()    {}

func (m *PartyServerInfo) GetServerIpAddress() string {
	if m != nil && m.ServerIpAddress != nil {
		return *m.ServerIpAddress
	}
	return ""
}

func (m *PartyServerInfo) GetServerPort() uint32 {
	if m != nil && m.ServerPort != nil {
		return *m.ServerPort
	}
	return 0
}

func (m *PartyServerInfo) GetGameHandle() int32 {
	if m != nil && m.GameHandle != nil {
		return *m.GameHandle
	}
	return 0
}

func (m *PartyServerInfo) GetSecretKey() string {
	if m != nil && m.SecretKey != nil {
		return *m.SecretKey
	}
	return ""
}

func (m *PartyServerInfo) GetGameType() PegasusShared.GameType {
	if m != nil && m.GameType != nil {
		return *m.GameType
	}
	return PegasusShared.GameType_GT_UNKNOWN
}

func (m *PartyServerInfo) GetMissionId() int32 {
	if m != nil && m.MissionId != nil {
		return *m.MissionId
	}
	return 0
}

func init() {
	proto.RegisterEnum("SpectatorProto.Constants", Constants_name, Constants_value)
}
