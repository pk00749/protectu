package com.warcraftyork.service;

import com.warcraftyork.bean.DBInfo;
import com.warcraftyork.mapper.PoliciesMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class PoliciesService {
    @Autowired
    private PoliciesMapper policiesMapper;

    @Transactional
    public String sayHello(String name){
        if(name == null){
            return "No Name to Select";
        }
        DBInfo info = policiesMapper.getDBInfo(name);

        try {
            System.out.println(info.getHost() + " " + info.getDb() + " " + info.getUser());
        } catch (Exception e) {
            e.printStackTrace();
//            sqlSession.rollback();
        } finally {
//            sqlSession.close();
        }
        return "Hello, " + info.getHost() + " " + info.getDb() + " " + info.getUser();
    }
}
