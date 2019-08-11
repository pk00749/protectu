package com.warcraftyork.controller;

import com.warcraftyork.bean.DBInfo;
import com.warcraftyork.mapper.PoliciesMapper;
import com.warcraftyork.protectu.DbUtils;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpSession;

@Controller
public class PoliciesController {

    @RequestMapping("/test")
    public String test(){
        return "index";
    }

    @RequestMapping(value = "/sayHello")
    @ResponseBody
    public String sayHello(String name){
        if(name == null){
            return "No Name to Select";
        }
        SqlSessionFactory factory = DbUtils.getSqlSessionFactory();
        SqlSession sqlSession = factory.openSession();
        PoliciesMapper testMapper = sqlSession.getMapper(PoliciesMapper.class);
        DBInfo info = testMapper.getDBInfo(name);

        try {
            System.out.println(info.getHost() + " " + info.getDb() + " " + info.getUser());
        } catch (Exception e) {
            e.printStackTrace();
            sqlSession.rollback();
        } finally {
            sqlSession.close();
        }
        return "Hello, " + info.getHost() + " " + info.getDb() + " " + info.getUser();
    }

    @GetMapping("/login")
    public String login(){
        return "login";
    }

    @RequestMapping("/policies")
    public String policies() {
        return "policies";
    }

    @RequestMapping("/logout")
    public String logout(HttpSession session){
//        session.removeAttribute(WebSecurityConfig.SESSION_KEY);
        return "redirect:/login";
    }
}
