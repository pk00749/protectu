package com.warcraftyork.service;

import com.warcraftyork.bean.DBInfo;
import com.warcraftyork.mapper.PoliciesMapper;
import com.warcraftyork.protectu.DbUtils;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PoliciesService {
//    @Autowired
    private PoliciesMapper policiesMapper;


    public String sayHello(String name){
        if(name == null){
            return "No Name to Select";
        }
        SqlSessionFactory factory = DbUtils.getSqlSessionFactory();
        SqlSession sqlSession = factory.openSession();
        PoliciesMapper policiesMapper = sqlSession.getMapper(PoliciesMapper.class);
        DBInfo info = policiesMapper.getDBInfo(name);

        try {
            System.out.println(info.getHost() + " " + info.getDb() + " " + info.getUser());
        } catch (Exception e) {
            e.printStackTrace();
            sqlSession.rollback();
        } finally {
            sqlSession.close();
        }
        return "Hello, " + info.getHost() + " " + info.getDb() + " " + info.getUser();
//        return name;
    }
}
