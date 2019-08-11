package com.warcraftyork.mapper;

import com.warcraftyork.bean.DBInfo;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface PoliciesMapper {
     DBInfo getDBInfo(String user);
}
